from fastapi import FastAPI

from app.core.database import engine, Base
from app.models.user import User  # IMPORTANT: ensures table is registered

from app.api.v1.endpoints.auth import router as auth_router

app = FastAPI(title="Ecommerce API")


# -----------------------
# AUTH ROUTES
# -----------------------
app.include_router(auth_router, prefix="/auth", tags=["Auth"])


# -----------------------
# ROOT ENDPOINT
# -----------------------
@app.get("/")
async def root():
    return {"message": "API is running"}


# -----------------------
# DB INITIALIZATION
# -----------------------
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)