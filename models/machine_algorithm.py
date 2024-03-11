from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class MachineAlgorithm(Base):
    __tablename__ = "tb_machine_algorithm"

    machine_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_machine.id"), primary_key=True)
    algorithm_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_algorithm.id"), primary_key=True)
