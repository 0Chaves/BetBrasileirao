from sqlalchemy import String, Integer, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship  
from database import Base
import datetime

class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key = True, index = True)
    status: Mapped[str] = mapped_column(String(255), index=True, nullable=False) #Marcado, em andamento, encerrado
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)

    # 1. Time da casa
    # Define a coluna que guardará o ID do time A no banco de dados
    home_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    # Cria a relação a nível de objeto no Python (permite fazer: game.team.name)
    home_team: Mapped["Team"] = relationship(back_populates="games_as_home_team", foreign_keys=[home_team_id])

    # 2. Time de fora
    away_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    away_team: Mapped["Team"] = relationship(back_populates="games_as_away_team", foreign_keys=[away_team_id])

    # 3. VENCEDOR
    winner_id: Mapped[int | None] = mapped_column(ForeignKey("teams.id"), nullable=True)
    winner: Mapped["Team"] = relationship(back_populates="won_games", foreign_keys=[winner_id])
    winner_str: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)

    # 4. GOLS
    home_team_goals: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    away_team_goals: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    # 5. BETS
    bets: Mapped[list["Bet"]] = relationship(back_populates="game", foreign_keys="[Bet.game_id]")