#TODO: revisar validações
from pydantic import BaseModel, ConfigDict, field_validator
from decimal import Decimal

class BetBase(BaseModel):
    points: Decimal
    prediction: str
    status: str
    multiplier: Decimal

    @field_validator('points')
    @classmethod
    def verify_points(cls, p: int):
        if p <= 0:
            raise ValueError ("Os pontos devem ser positivos")
        return p

class BetCreate(BetBase):
    user_id: int
    game_id: int

class BetUpdate(BaseModel):
    points: Decimal | None = None
    prediction: str | None = None
    status: str | None = None
    multiplier: Decimal | None = None

class BetResponse(BetBase):
    id: int
    user_id: int
    game_id: int

    model_config = ConfigDict(from_attributes=True)