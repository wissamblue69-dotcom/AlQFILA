import os

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
