import datetime
from decimal import Decimal
from sqlalchemy import String, Text, Boolean, Integer, Numeric, Date, ForeignKey
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
    senha: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    points: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=Decimal("1000.00"))
    max_points: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False, default=Decimal("1000.00"))
    right_calls: Mapped[int] = mapped_column(Integer, nullable=False)
    bets: Mapped[list["Bet"]] = relationship(back_populates="user", foreign_keys="[Bet.user_id]")

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

class Bet(Base):
    __tablename__ = "bets"

    id: Mapped[int] = mapped_column(primary_key = True, index = True)
    points: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    prediction: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False) #em andamento, finalizada
    multiplier: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="bets", foreign_keys=[user_id])

    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"), nullable=False)
    game: Mapped["Game"] = relationship(back_populates="bets", foreign_keys=[game_id])