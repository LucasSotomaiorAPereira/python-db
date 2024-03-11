from typing import Optional, List
from sqlalchemy import String, Integer, DateTime, Float, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from datetime import datetime
from services.db import session
from sqlalchemy.sql import text


class Product(Base):
    __tablename__ = "tb_product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    orders: Mapped[List["Order"]] = relationship(  # type: ignore
        "Order", secondary="tb_order_product", back_populates="products", uselist=True)

    def getStock(self, id: int):
        statement = select(Product.stock).where(Product.id == id)
        return session.execute(statement).fetchone()

    def getPrice(self, id: int):
        statement = select(Product.price).where(Product.id == id)
        return session.execute(statement).fetchone()

    def getMostBuyedProducts(self):
        statement = text(
            "SELECT COUNT(product_id), product_id FROM tb_order_product GROUP BY product_id ORDER BY COUNT(product_id) DESC")
        return session.execute(statement).all()
