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
from app.models.cart import Cart
from app.models.product import Product
from app.models.order import Order

from app.schemas.order import OrderResponse

router = APIRouter()


async def get_db():
    async with SessionLocal() as session:
        yield session


@router.post("/place-order", response_model=OrderResponse)
async def place_order(
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

    cart_result = await db.execute(
        select(Cart).where(
            Cart.user_id == user.id
        )
    )

    cart_items = cart_result.scalars().all()

    if not cart_items:
        raise HTTPException(
            status_code=400,
            detail="Cart is empty"
        )

    total_amount = 0

    for item in cart_items:

        product_result = await db.execute(
            select(Product).where(
                Product.id == item.product_id
            )
        )

        product = product_result.scalar_one()

        total_amount += (
            product.price * item.quantity
        )

    order = Order(
        user_id=user.id,
        total_amount=total_amount
    )

    db.add(order)

    await db.commit()

    await db.refresh(order)

    for item in cart_items:
        await db.delete(item)

    await db.commit()

    return order


@router.get("/", response_model=list[OrderResponse])
async def list_orders(
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
        select(Order).where(
            Order.user_id == user.id
        )
    )

    return result.scalars().all()
