from sqlalchemy import Integer, Enum, ForeignKey, select
from sqlalchemy.sql import text
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base
from models.enum.client_type import ClientType
from services.db import session


class Client(Base):
    __tablename__ = "tb_client"

    person_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_person.id"), primary_key=True)
    type: Mapped[ClientType] = mapped_column(Enum(ClientType), nullable=False)

    def getType(self, id: int):
        statement = select(Client.type).where(Client.person_id == id)
        return session.execute(statement).fetchone()

    def getNumberOfClients(self):
        statement = select(Client)
        return len(session.execute(statement).all())

    def getAllClientsBets(self):
        statement = text(
            "SELECT b.* FROM tb_client AS c INNER JOIN tb_person AS p ON c.person_id = p.id INNER JOIN tb_bet AS b ON p.id = b.person_id")
        return session.execute(statement).all()

    def __repr__(self) -> str:
        return f"Client[person_id={self.person_id}, type={self.type}]"
