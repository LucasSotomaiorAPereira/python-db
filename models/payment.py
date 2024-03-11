from sqlalchemy import Integer, Float, DateTime, ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base
from datetime import datetime
from services.db import session


class Payment(Base):
    __tablename__ = "tb_payment"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    employee_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tb_employee.person_id"), nullable=False)

    def getEmployeePayment(self, id):
        statement = select(Payment.value).where(Payment.employee_id == id)
        return session.execute(statement).all()
