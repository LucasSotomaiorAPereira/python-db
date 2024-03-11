from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class BoardGame(Base):
    __tablename__ = "tb_board_game"

    board_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_board.id"), primary_key=True)
    game_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_game.id"), primary_key=True)
