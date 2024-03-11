from typing import List
from sqlalchemy import Integer, Enum, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import text
from models.base import Base
from models.enum.emp_function import EmployeeFunction
from services.db import session


class Employee(Base):
    __tablename__ = "tb_employee"

    person_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_person.id"), primary_key=True)
    function: Mapped[EmployeeFunction] = mapped_column(
        Enum(EmployeeFunction), nullable=False)
    boards: Mapped[List["Board"]] = relationship(  # type: ignore
        "Board", secondary="tb_board_employee", back_populates="employees", uselist=True)

    def getFunction(self, id: int):
        statement = select(Employee.function).where(Employee.person_id == id)
        return session.execute(statement).fetchone()

    def getNumberOfEmployees(self):
        statement = select(Employee)
        return len(session.execute(statement).all())

    def getNumberOfEmployeePayments(self, employee_id: int):
        statement = text(
            f"SELECT COUNT(*) FROM tb_employee AS e INNER JOIN tb_payment AS p ON p.employee_id = e.person_id GROUP BY employee_id HAVING employee_id={employee_id};")
        return session.execute(statement).all()

    def getWaitersData(self):
        statement = text(
            "SELECT p.* FROM tb_employee AS e INNER JOIN tb_person AS p ON p.id = e.person_id WHERE e.function='WAITER'")
        return session.execute(statement).all()

    def __repr__(self) -> str:
        return f"Employee[person_id={self.person_id}, function={self.function}]"
