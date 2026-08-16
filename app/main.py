from fastapi import FastAPI

app = FastAPI(title="AlQFILA Core Execution Service", version="0.1.0")


@app.get("/health", tags=["operations"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
