from typing import List
from sqlalchemy import Integer, DateTime, Enum, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from datetime import datetime
from models.enum.order_status import OrderStatus
from services.db import session


class Order(Base):
    __tablename__ = "tb_order"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus), nullable=False)
    services: Mapped[List["Service"]] = relationship(  # type: ignore
        "Service", secondary="tb_order_service", back_populates="orders", uselist=True)
    products: Mapped[List["Product"]] = relationship(  # type: ignore
        "Product", secondary="tb_order_product", back_populates="orders", uselist=True)
    charge: Mapped[List["Charge"]] = relationship(  # type: ignore
        "Charge", secondary="tb_order_charge", back_populates="order", uselist=True)
    person_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_person.id"))

    def getStatus(self, id: int):
        statement = select(Order.status).where(Order.id == id)
        return session.execute(statement).fetchone()
