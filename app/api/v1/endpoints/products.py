from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import SessionLocal
from app.models.product import Product
from app.schemas.product import (
    ProductCreate,
    ProductResponse
)

router = APIRouter()


# Database Dependency
async def get_db():
    async with SessionLocal() as session:
        yield session


# CREATE PRODUCT
@router.post("/", response_model=ProductResponse)
async def create_product(
    product: ProductCreate,
    db: AsyncSession = Depends(get_db)
):

    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
        category_id=product.category_id
    )

    db.add(new_product)

    await db.commit()

    await db.refresh(new_product)

    return new_product


# LIST PRODUCTS
@router.get("/", response_model=list[ProductResponse])
async def list_products(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Product)
    )

    products = result.scalars().all()

    return products