#TODO: revisar validações
from pydantic import BaseModel, ConfigDict, field_validator
from decimal import Decimal
from schemas.team_schema import TeamResponse
from datetime import date

class GameBase(BaseModel):
    id: int
    status: str
    date: date
    home_team_goals: int | None
    away_team_goals: int | None
    winner_str: str | None

# Na criação, o cliente envia apenas as chaves estrangeiras
class GameCreate(GameBase):
    home_team_id: int
    away_team_id: int
    winner_id: int | None

class GameUpdate(BaseModel):
    status: str | None = None
    home_team_goals: int | None = None
    away_team_goals: int | None = None
    winner_id: int | None = None
    winner_str: str | None = None

class BetSummary(BaseModel):
    id: int
    points: Decimal
    prediction: str
    status: str
    multiplier: Decimal
    user_id: int

# Na resposta, podemos aninhar os Schemas de Time para devolver os dados completos!
class GameResponse(GameBase):
    winner_id: int | None = None
    
    # Ao incluir os schemas aqui, o FastAPI pede para o SQLAlchemy:
    # "Vá buscar os dados dos times e monte um JSON aninhado!"
    home_team: TeamResponse
    away_team: TeamResponse
    winner: TeamResponse | None = None

    bets:list[BetSummary] = []

    model_config = ConfigDict(from_attributes=True)