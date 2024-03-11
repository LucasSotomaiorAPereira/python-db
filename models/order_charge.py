from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class OrderCharge(Base):
    __tablename__ = "tb_order_charge"

    order_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_order.id"), primary_key=True)
    charge_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_charge.id"), primary_key=True)
