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
    
    games_as_home_team: Mapped[list["Game"]] = relationship(back_populates="home_team", foreign_keys="[Game.home_team_id]")
    games_as_away_team: Mapped[list["Game"]] = relationship(back_populates="away_team", foreign_keys="[Game.away_team_id]")
    won_games: Mapped[list["Game"]] = relationship(back_populates="winner", foreign_keys="[Game.winner_id]")