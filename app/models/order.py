from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
    DateTime,
    func
)

from sqlalchemy.orm import relationship

from app.core.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    total_amount = Column(
        Float,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship(
        "User"
    )