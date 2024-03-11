from typing import Optional, List
from sqlalchemy import Integer, String, DateTime, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from datetime import datetime
from services.db import session
from sqlalchemy.sql import text


class Charge(Base):
    __tablename__ = "tb_charge"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    order: Mapped[List["Order"]] = relationship(  # type: ignore
        "Order", secondary="tb_order_charge", back_populates="charge", uselist=True)

    def getCreationDate(self, id: int):
        statement = select(Charge.created_at).where(Charge.id == id)
        return session.execute(statement).fetchone()

    def getMostUsedCharges(self):
        statement = text(
            "SELECT COUNT(charge_id), charge_id FROM tb_order_charge GROUP BY charge_id ORDER BY COUNT(charge_id) DESC")
        return session.execute(statement)
