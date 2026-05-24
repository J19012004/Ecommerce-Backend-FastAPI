from fastapi import FastAPI
from app.core.database import engine

app = FastAPI(title="Ecommerce API")


# Root route (health check)
@app.get("/")
async def root():
    return {"message": "API is running"}


# DB connection test (safe endpoint)
@app.get("/db-check")
async def db_check():
    async with engine.begin() as conn:
        await conn.run_sync(lambda _: None)
    return {"message": "DB connection successful"}