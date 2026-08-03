#TODO: revisar validações
from pydantic import BaseModel, ConfigDict, field_validator
from datetime import date
import re
from decimal import Decimal


# Atributos compartilhados tanto na criação quanto na visualização
class TeamBase(BaseModel):
    name: str
    flag: str
    code: str
    group: str
    wins: int = 0
    losses: int = 0
    draws: int = 0
    
# Schema para validação ao CRIAR (entrada do POST)
class TeamCreate(TeamBase):
    pass

# Schema para validação ao ATUALIZAR (entrada do PUT)
class TeamUpdate(BaseModel):
    nome: str | None = None
    bandeira: str | None = None
    sigla: str | None = None
    grupo: str | None = None
    vitorias: int | None = None
    derrotas: int | None = None
    empates: int | None = None

# Necessario para evitar looping infinito no json
class GameSummary(BaseModel):
    id: int
    status: str
    teamA_id: int
    teamB_id: int
    teamA_goals: int
    teamB_goals: int
    
    model_config = ConfigDict(from_attributes=True)

# Schema para RETORNAR (saída das rotas)
class TeamResponse(TeamBase):
    id: int

    # O SQLAlchemy preenche essas listas automaticamente através dos 'relationships'
    games_as_team_a: list[GameSummary] = []
    games_as_team_b: list[GameSummary] = []
    won_games: list[GameSummary] = []
    model_config = ConfigDict(from_attributes=True)