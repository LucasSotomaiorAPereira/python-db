from typing import Optional, List
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from models.base import Base


class Algorithm(Base):
    __tablename__ = "tb_algorithm"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(
        String(255), nullable=True)
    code_url: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    machines: Mapped[List["Machine"]] = relationship(  # type: ignore
        "Machine", secondary="tb_machine_algorithm", back_populates="algorithms", uselist=True)
