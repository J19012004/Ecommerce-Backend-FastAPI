from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import SessionLocal
from app.core.security import get_current_user

from app.models.user import User
from app.models.product import Product
from app.models.cart import Cart

from app.schemas.cart import (
    CartCreate,
    CartResponse
)

router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@router.post("/add", response_model=CartResponse)
async def add_to_cart(
    item: CartCreate,
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    user_result = await db.execute(
        select(User).where(
            User.email == current_user
        )
    )

    user = user_result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    product_result = await db.execute(
        select(Product).where(
            Product.id == item.product_id
        )
    )

    product = product_result.scalar_one_or_none()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    cart_item = Cart(
        user_id=user.id,
        product_id=item.product_id,
        quantity=item.quantity
    )

    db.add(cart_item)

    await db.commit()

    await db.refresh(cart_item)

    return cart_item


@router.get("/", response_model=list[CartResponse])
async def view_cart(
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    user_result = await db.execute(
        select(User).where(
            User.email == current_user
        )
    )

    user = user_result.scalar_one_or_none()

    result = await db.execute(
        select(Cart).where(
            Cart.user_id == user.id
        )
    )

    return result.scalars().all()


@router.delete("/{cart_id}")
async def remove_from_cart(
    cart_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    result = await db.execute(
        select(Cart).where(
            Cart.id == cart_id
        )
    )

    cart_item = result.scalar_one_or_none()

    if not cart_item:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )

    await db.delete(cart_item)

    await db.commit()

    return {
        "message": "Item removed from cart"
    }