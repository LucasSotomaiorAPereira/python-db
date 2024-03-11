from typing import List
from sqlalchemy import Integer, ForeignKey, Boolean, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from services.db import session


class Board(Base):
    __tablename__ = "tb_board"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    number: Mapped[int] = mapped_column(
        Integer, nullable=False, unique=True)
    available: Mapped[bool] = mapped_column(Boolean, nullable=False)
    employees: Mapped[List["Employee"]] = relationship(  # type: ignore
        "Employee", secondary="tb_board_employee", back_populates="boards", uselist=True)
    games: Mapped[List["Game"]] = relationship(  # type: ignore
        "Game", secondary="tb_board_game", back_populates="boards", uselist=True)
    branch_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_branch.id"))

    def getAvailable(self, id: int):
        statement = select(Board.available).where(Board.id == id)
        return session.execute(statement).fetchone()
