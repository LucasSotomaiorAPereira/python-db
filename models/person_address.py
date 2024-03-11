from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class PersonAddress(Base):
    __tablename__ = "tb_person_address"

    person_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_person.id"), primary_key=True)
    address_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_address.id"), primary_key=True)
