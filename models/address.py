from typing import List
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base


class Address(Base):
    __tablename__ = "tb_address"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    street: Mapped[str] = mapped_column(String(255), nullable=False)
    district: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(80), nullable=False)
    state: Mapped[str] = mapped_column(String(50), nullable=False)
    country: Mapped[str] = mapped_column(String(50), nullable=False)
    persons: Mapped[List["Person"]] = relationship(  # type: ignore
        "Person", secondary="tb_person_address", back_populates="addresses", uselist=True)
