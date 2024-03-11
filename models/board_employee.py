from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class BoardEmployee(Base):
    __tablename__ = "tb_board_employee"

    board_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_board.id"), primary_key=True)
    employee_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_employee.person_id"), primary_key=True)
