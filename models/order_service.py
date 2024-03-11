from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class OrderService(Base):
    __tablename__ = "tb_order_service"

    order_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_order.id"), primary_key=True)
    service_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_service.id"), primary_key=True)
