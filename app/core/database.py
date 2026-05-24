from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from app.core.config import settings

# Create async PostgreSQL engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # shows SQL in terminal (good for learning/debugging)
    pool_pre_ping=True  # helps avoid stale connections
)

# Session factory (used in routes later)
SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

# Base class for all ORM models
Base = declarative_base()