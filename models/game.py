from typing import List
from sqlalchemy import Integer, String, Float, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from services.db import session
from sqlalchemy.sql import text


class Game(Base):
    __tablename__ = "tb_game"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    max_players: Mapped[int] = mapped_column(Integer, nullable=True)
    min_players: Mapped[int] = mapped_column(Integer, nullable=True)
    max_bet: Mapped[float] = mapped_column(Float, nullable=False)
    min_bet: Mapped[float] = mapped_column(Float, nullable=False)
    boards: Mapped[List["Board"]] = relationship(  # type: ignore
        "Board", secondary="tb_board_game", back_populates="games", uselist=True)

    def getMostUsedGames(self):
        statement = text(
            "SELECT COUNT(game_id), game_id FROM tb_bet WHERE game_id IS NOT NULL GROUP BY game_id ORDER BY COUNT(game_id) DESC")
        return session.execute(statement).all()
