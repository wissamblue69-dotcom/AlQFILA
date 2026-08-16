import os

import aioredis
from aiokafka import AIOKafkaProducer
from fastapi import HTTPException

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

cors_origins = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ALLOW_ORIGINS",
        "http://localhost:3000,http://127.0.0.1:3000",
    ).split(",")
    if origin.strip()
]

app = FastAPI(
    title="AlQFILA Core API",
    version="0.1.0",
    contact={
        "name": "Wissam Hajj Mohammad",
        "url": "https://github.com/wissamblue69-dotcom/qafila-systems-architecture",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=[],
)


@app.get("/health", tags=["operations"])
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "alqfila-core"}


@app.get("/health/redis", tags=["operations"])
async def redis_health() -> dict[str, str]:
    redis = aioredis.from_url(os.getenv("REDIS_URL", "redis://redis:6379/0"))
    try:
        await redis.ping()
    except Exception as error:
        raise HTTPException(status_code=503, detail="Redis health check failed") from error
    finally:
        await redis.close()

    return {"status": "ok", "service": "redis"}


@app.get("/health/kafka", tags=["operations"])
async def kafka_health() -> dict[str, str]:
    producer = AIOKafkaProducer(
        bootstrap_servers=os.getenv("KAFKA_BROKER", "kafka:9092"),
        request_timeout_ms=3000,
    )
    try:
        await producer.start()
    except Exception as error:
        raise HTTPException(status_code=503, detail="Kafka health check failed") from error
    finally:
        await producer.stop()

    return {"status": "ok", "service": "kafka"}
