from typing import Optional, List
from sqlalchemy import String, Integer, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from datetime import datetime


class Service(Base):
    __tablename__ = "tb_service"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    orders: Mapped[List["Order"]] = relationship(  # type: ignore
        "Order", secondary="tb_order_service", back_populates="services", uselist=True)
