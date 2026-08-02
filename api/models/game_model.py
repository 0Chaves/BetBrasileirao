from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship  
from database import Base

class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = mapped_column(primary_key = True, index = True)
    status: Mapped[str] = mapped_column(String(255), index=True, nullable=False) #Marcado, em andamento, encerrado
        
    # 1. TIME A
    # Define a coluna que guardará o ID do time A no banco de dados
    teamA_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    # Cria a relação a nível de objeto no Python (permite fazer: game.team.name)
    teamA: Mapped["Team"] = relationship(back_populates="games_as_team_a", foreign_keys=[teamA_id])

    # 2. TIME B
    teamB_id: Mapped[int] = mapped_column(ForeignKey("teams.id"), nullable=False)
    teamB: Mapped["Team"] = relationship(back_populates="games_as_team_b", foreign_keys=[teamB_id])

    # 3. VENCEDOR
    winner_id: Mapped[int | None] = mapped_column(ForeignKey("teams.id"), nullable=True)
    winner: Mapped["Team"] = relationship(back_populates="won_games", foreign_keys=[winner_id])

    # 4. GOLS
    teamA_goals: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    teamB_goals: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    # 5. BETS
    bets: Mapped[list["Bet"]] = relationship(back_populates="game", foreign_keys="[Bet.game_id]")