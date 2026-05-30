from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import SessionLocal
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user,
)

from app.models.user import User
from app.schemas.user import UserCreate, UserLogin

router = APIRouter()


# -------------------------
# DATABASE DEPENDENCY
# -------------------------
async def get_db():
    async with SessionLocal() as session:
        yield session


# -------------------------
# REGISTER
# -------------------------
@router.post("/register")
async def register(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(User.email == user.email)
    )

    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)

    await db.commit()

    return {
        "message": "User registered successfully"
    }


# -------------------------
# LOGIN
# -------------------------
@router.post("/login")
async def login(
    user: UserLogin,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(User.email == user.email)
    )

    db_user = result.scalar_one_or_none()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    valid_password = verify_password(
        user.password,
        db_user.hashed_password
    )

    if not valid_password:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token(
        data={
            "sub": db_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# -------------------------
# CURRENT USER
# -------------------------
@router.get("/me")
async def get_me(
    current_user: str = Depends(get_current_user)
):
    return {
        "email": current_user
    }