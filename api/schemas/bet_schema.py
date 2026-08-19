#TODO: revisar validações
from pydantic import BaseModel, ConfigDict, field_validator
from decimal import Decimal

class BetBase(BaseModel):
    points: Decimal
    prediction: str

    @field_validator('points')
    @classmethod
    def verify_points(cls, p: Decimal):
        if p <= 0:
            raise ValueError("Os pontos devem ser positivos")
        return p

class BetCreate(BetBase):
    game_id: int

class BetUpdate(BaseModel):
    points: Decimal | None = None
    prediction: str | None = None
    status: str | None = None

class BetResponse(BetBase):
    id: int
    status: str
    multiplier: Decimal
    user_id: int
    game_id: int

    model_config = ConfigDict(from_attributes=True)