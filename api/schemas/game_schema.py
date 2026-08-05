#TODO: revisar validações
from pydantic import BaseModel, ConfigDict, field_validator
from decimal import Decimal
from schemas.team_schema import TeamResponse

class GameBase(BaseModel):
    status: str
    teamA_goals: int = 0
    teamB_goals: int = 0

# Na criação, o cliente envia apenas as chaves estrangeiras
class GameCreate(GameBase):
    teamA_id: int
    teamB_id: int
    # winner_id não é enviado na criação, pois o jogo acabou de ser marcado

class GameUpdate(BaseModel):
    status: str | None = None
    teamA_goals: int | None = None
    teamB_goals: int | None = None
    winner_id: int | None = None

class BetSummary(BaseModel):
    id: int
    points: Decimal
    prediction: str
    status: str
    multiplier: Decimal
    user_id: int

# Na resposta, podemos aninhar os Schemas de Time para devolver os dados completos!
class GameResponse(GameBase):
    id: int
    winner_id: int | None = None
    
    # Ao incluir os schemas aqui, o FastAPI pede para o SQLAlchemy:
    # "Vá buscar os dados dos times e monte um JSON aninhado!"
    teamA: TeamResponse
    teamB: TeamResponse
    winner: TeamResponse | None = None

    bets:list[BetSummary] = []

    model_config = ConfigDict(from_attributes=True)