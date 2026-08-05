import datetime
from decimal import Decimal
from sqlalchemy import String, Boolean, Integer, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship  
from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    isAdmin: Mapped[bool] = mapped_column(Boolean, default=False)
    isActive: Mapped[bool] = mapped_column(Boolean, default=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    cpf: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    birthDate: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    login: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    points: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=Decimal("1000.00"))
    max_points: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=Decimal("1000.00"))
    right_calls: Mapped[int] = mapped_column(Integer, nullable=False)
    bets: Mapped[list["Bet"]] = relationship(back_populates="user", foreign_keys="[Bet.user_id]")