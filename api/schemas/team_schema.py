#TODO: revisar validações
from pydantic import BaseModel, ConfigDict, field_validator

# Atributos compartilhados tanto na criação quanto na visualização
class TeamBase(BaseModel):
    id: int
    name: str
    flag: str
    code: str
    position: int
    playedGames: int
    won: int
    lost: int
    draw: int
    points: int
    
# Schema para validação ao CRIAR (entrada do POST)
class TeamCreate(TeamBase):
    pass

# Schema para validação ao ATUALIZAR (entrada do PUT)
class TeamUpdate(BaseModel):
    name: str | None = None
    flag: str | None = None
    code: str | None = None
    position: int | None = None
    playedGames: int | None = None
    won: int | None = None
    lost: int | None = None
    draw: int | None = None
    points: int | None = None

# Necessario para evitar looping infinito no json
class GameSummary(BaseModel):
    id: int
    status: str
    home_team_id: int
    away_team_id: int
    home_team_goals: int
    away_team_goals: int
    
    model_config = ConfigDict(from_attributes=True)

# Schema para RETORNAR (saída das rotas)
class TeamResponse(TeamBase):
    # O SQLAlchemy preenche essas listas automaticamente através dos 'relationships'
    games_as_home_team: list[GameSummary] = []
    games_as_away_team: list[GameSummary] = []
    won_games: list[GameSummary] = []
    model_config = ConfigDict(from_attributes=True)