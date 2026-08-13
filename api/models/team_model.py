from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship  
from database import Base

class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    flag: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    code: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    position: Mapped[int] = mapped_column(Integer)
    playedGames: Mapped[int] = mapped_column(Integer)
    won: Mapped[int] = mapped_column(Integer)
    lost: Mapped[int] = mapped_column(Integer)
    draw: Mapped[int] = mapped_column(Integer)
    points: Mapped[int] = mapped_column(Integer)
    
    games_as_team_a: Mapped[list["Game"]] = relationship(back_populates="teamA", foreign_keys="[Game.teamA_id]")
    games_as_team_b: Mapped[list["Game"]] = relationship(back_populates="teamB", foreign_keys="[Game.teamB_id]")
    won_games: Mapped[list["Game"]] = relationship(back_populates="winner", foreign_keys="[Game.winner_id]")