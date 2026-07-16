from sqlalchemy import String, Text, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Projeto(Base):
    __tablename__ = "projetos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)
    ativo: Mapped[bool] = mapped_column(Boolean, default=True)

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