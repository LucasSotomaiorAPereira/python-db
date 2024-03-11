from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class Branch(Base):
    __tablename__ = "tb_branch"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    cnpj: Mapped[str] = mapped_column(String(25), nullable=False, unique=True)
    address_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_address.id"))
