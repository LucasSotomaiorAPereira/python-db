from sqlalchemy import ForeignKey, Integer, String, Date, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from typing import List
from datetime import date
from sqlalchemy.sql import text
from services.db import session


class Person(Base):
    __tablename__ = "tb_person"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    lastname: Mapped[str] = mapped_column(String(255), nullable=False)
    cpf: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True)
    birthdate: Mapped[date] = mapped_column(Date, nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    addresses: Mapped[List["Address"]] = relationship(  # type: ignore
        "Address", secondary="tb_person_address", back_populates="persons", uselist=True)
    branch_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_branch.id"))

    def getBets(self, id: int):
        statement = text(f"SELECT * FROM tb_bet WHERE person_id = {id}")
        return session.execute(statement).all()

    def getPersonBetsValue(self, id: int):
        statement = text(
            f"SELECT SUM(value) FROM tb_bet WHERE person_id = {id} GROUP BY person_id")
        return session.execute(statement).fetchone()

    def getThreeMostBetPeople(self):
        statement = text(
            "SELECT SUM(value), person_id FROM tb_bet GROUP BY person_id ORDER BY SUM(value) DESC LIMIT 3")
        return session.execute(statement).all()

    def getNumberOfPeopleInAddress(self, address_id: int):
        statement = text(
            f"SELECT COUNT(*) FROM tb_person_address GROUP BY address_id HAVING address_id={address_id}")
        return session.execute(statement).all()

    def getNumberOfPersonOrders(self, person_id: int):
        statement = text(
            f"SELECT COUNT(*) FROM tb_person AS p INNER JOIN tb_order AS o ON p.id = o.person_id GROUP BY person_id HAVING person_id={person_id}")
        return session.execute(statement).all()

    def getPersonWinRate(self, id: int):
        statement = text(
            f"SELECT AVG(win) FROM tb_bet WHERE person_id = {id} GROUP BY person_id")
        result = session.execute(statement).fetchone()
        return result[0] * 100  # type: ignore

    def __repr__(self) -> str:
        return f"Person[name={self.name}, lastname={self.lastname}, cpf={self.cpf}, " \
            + f"rg={self.rg}, email={self.email}, birthdate={self.birthdate}, {self.phone}, " \
            + f"branch_id={self.branch_id}]"
