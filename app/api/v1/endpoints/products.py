from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import SessionLocal
from app.core.security import get_current_user

from app.models.product import Product

from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

router = APIRouter()


# -------------------------
# DATABASE DEPENDENCY
# -------------------------
async def get_db():
    async with SessionLocal() as session:
        yield session


# -------------------------
# CREATE PRODUCT
# -------------------------
@router.post("/", response_model=ProductResponse)
async def create_product(
    product: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
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


# -------------------------
# LIST PRODUCTS
# -------------------------
@router.get("/", response_model=list[ProductResponse])
async def list_products(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Product)
    )

    products = result.scalars().all()

    return products


# -------------------------
# GET PRODUCT BY ID
# -------------------------
@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Product).where(
            Product.id == product_id
        )
    )

    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# -------------------------
# UPDATE PRODUCT
# -------------------------
@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int,
    product_data: ProductUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    result = await db.execute(
        select(Product).where(
            Product.id == product_id
        )
    )

    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product.name = product_data.name
    product.description = product_data.description
    product.price = product_data.price
    product.stock = product_data.stock
    product.category_id = product_data.category_id

    await db.commit()

    await db.refresh(product)

    return product


# -------------------------
# DELETE PRODUCT
# -------------------------
@router.delete("/{product_id}")
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    result = await db.execute(
        select(Product).where(
            Product.id == product_id
        )
    )

    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    await db.delete(product)

    await db.commit()

    return {
        "message": "Product deleted successfully"
    }