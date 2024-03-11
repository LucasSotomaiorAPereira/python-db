from typing import Optional, List
from sqlalchemy import String, Integer, DateTime, Boolean, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import text
from datetime import datetime
from models.base import Base
from services.db import session


class Machine(Base):
    __tablename__ = "tb_machine"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    activated: Mapped[bool] = mapped_column(Boolean, nullable=False)
    algorithms: Mapped[List["Algorithm"]] = relationship(  # type: ignore
        "Algorithm", secondary="tb_machine_algorithm", back_populates="machines", uselist=True)
    branch_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_branch.id"))

    def getActive(self, id: int):
        statement = select(Machine.activated).where(Machine.id == id)
        return session.execute(statement).fetchone()

    def getMostUsedMachines(self):
        statement = text(
            "SELECT COUNT(machine_id), machine_id FROM tb_bet WHERE machine_id IS NOT NULL GROUP BY machine_id ORDER BY COUNT(machine_id) DESC")
        return session.execute(statement).all()

    def getAllMachinesBets(self):
        statement = text(
            f"SELECT b.* FROM tb_machine AS m INNER JOIN tb_bet AS b ON m.id = b.machine_id")
        return session.execute(statement).all()

    def __repr__(self) -> str:
        return f"Machine[name={self.name}, description={self.description}, created_at={self.created_at}, " \
            + f"activated={self.activated}, branch_id={self.branch_id}]"
