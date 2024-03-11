from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class OrderProduct(Base):
    __tablename__ = "tb_order_product"

    order_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_order.id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_product.id"), primary_key=True)
