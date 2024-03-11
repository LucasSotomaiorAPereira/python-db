from sqlalchemy import Integer, Float, DateTime, ForeignKey, Boolean, select
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import text
from models.base import Base
from datetime import datetime
from services.db import session


class Bet(Base):
    __tablename__ = "tb_bet"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    win: Mapped[bool] = mapped_column(Boolean, nullable=False)
    game_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_game.id"), nullable=True)
    machine_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_machine.id"), nullable=True)
    person_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_person.id"))

    def getBetValue(self, id: int):
        statement = select(Bet.value).where(Bet.id == id)
        return session.execute(statement).fetchone()

    def __repr__(self) -> str:
        return f"Bet[id={self.id}, value={self.value}, created_at={self.created_at}, " \
            + f"game_id={self.game_id}, machine_id={self.machine_id}, person_id={self.person_id}]"
