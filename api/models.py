from sqlalchemy import String, Text, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Team(Base):
    __tablename__ = "times"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    bandeira: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    sigla: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    grupo: Mapped[str] = mapped_column(String(1), default=True)
    vitorias: Mapped[int] = mapped_column(Integer, nullable=False)
    derrotas: Mapped[int] = mapped_column(Integer, nullable=False)
    empates: Mapped[int] = mapped_column(Integer, nullable=False)

class Usuario(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    isAdmin: Mapped[bool] = mapped_column(Boolean, default=False)
    statusAtivo: Mapped[bool] = mapped_column(Boolean, default=True)
    nome: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    cpf: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    dataNascimento: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    login: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    pontos: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=Decimal("0.00"))
    pontos_maximo: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=Decimal("0.00"))
    totalAcertos: Mapped[int] = mapped_column(Integer, nullable=False)