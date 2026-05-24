from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import SessionLocal
from app.models.category import Category
from app.schemas.category import (
    CategoryCreate,
    CategoryResponse
)

router = APIRouter()


# Database Dependency
async def get_db():
    async with SessionLocal() as session:
        yield session


# CREATE CATEGORY
@router.post("/", response_model=CategoryResponse)
async def create_category(
    category: CategoryCreate,
    db: AsyncSession = Depends(get_db)
):

    new_category = Category(
        name=category.name
    )

    db.add(new_category)

    await db.commit()

    await db.refresh(new_category)

    return new_category


# LIST CATEGORIES
@router.get("/", response_model=list[CategoryResponse])
async def list_categories(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Category)
    )

    categories = result.scalars().all()

    return categories