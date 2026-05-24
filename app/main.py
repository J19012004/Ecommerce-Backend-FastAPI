from fastapi import FastAPI

from app.core.database import engine, Base

# Import models so SQLAlchemy registers tables
from app.models.user import User
from app.models.category import Category
from app.models.product import Product

# Routers
from app.api.v1.endpoints.auth import router as auth_router

app = FastAPI(title="Ecommerce API")


# -----------------------------
# ROUTERS
# -----------------------------
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]
)


# -----------------------------
# ROOT ENDPOINT
# -----------------------------
@app.get("/")
async def root():
    return {"message": "Ecommerce API is running"}


# -----------------------------
# DB CHECK ENDPOINT
# -----------------------------
@app.get("/db-check")
async def db_check():
    async with engine.begin() as conn:
        await conn.run_sync(lambda _: None)

    return {"message": "Database connection successful"}


# -----------------------------
# STARTUP EVENT
# -----------------------------
@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)