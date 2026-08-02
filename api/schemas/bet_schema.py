#TODO: revisar validações
from pydantic import BaseModel, ConfigDict, field_validator
from datetime import date
import re
from decimal import Decimal

class BetBase(BaseModel):
    points: Decimal
    prediction: str
    status: str
    multiplier: Decimal

class BetCreate(BetBase):
    pass

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