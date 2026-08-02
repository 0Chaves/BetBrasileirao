from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship  
from database import Base

class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    flag: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    code: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    group: Mapped[str] = mapped_column(String(1))
    wins: Mapped[int] = mapped_column(Integer, nullable=False, default = 0)
    losses: Mapped[int] = mapped_column(Integer, nullable=False, default = 0)
    draws: Mapped[int] = mapped_column(Integer, nullable=False, default = 0)
    
    games_as_team_a: Mapped[list["Game"]] = relationship(back_populates="teamA", foreign_keys="[Game.teamA_id]")
    games_as_team_b: Mapped[list["Game"]] = relationship(back_populates="teamB", foreign_keys="[Game.teamB_id]")
    won_games: Mapped[list["Game"]] = relationship(back_populates="winner", foreign_keys="[Game.winner_id]")