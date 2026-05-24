from fastapi import FastAPI

from app.core.database import engine, Base

# Import models so SQLAlchemy creates tables
from app.models.user import User
from app.models.product import Product
from app.models.category import Category

# Routers
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.products import router as product_router
from app.api.v1.endpoints.categories import router as category_router

app = FastAPI(title="Ecommerce API")


# -----------------------------
# ROOT ENDPOINT
# -----------------------------
@app.get("/")
async def root():
    return {"message": "Ecommerce API is running"}


# -----------------------------
# DATABASE CHECK
# -----------------------------
@app.get("/db-check")
async def db_check():

    async with engine.begin() as conn:
        await conn.run_sync(lambda _: None)

    return {
        "message": "Database connection successful"
    }


# -----------------------------
# ROUTERS
# -----------------------------
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]
)

app.include_router(
    product_router,
    prefix="/products",
    tags=["Products"]
)

app.include_router(
    category_router,
    prefix="/categories",
    tags=["Categories"]
)


# -----------------------------
# STARTUP EVENT
# -----------------------------
@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )