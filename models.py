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