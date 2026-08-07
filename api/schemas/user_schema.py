#TODO: revisar validações
from pydantic import BaseModel, ConfigDict, field_validator
from datetime import date
import re
from decimal import Decimal
from schemas.game_schema import GameResponse

class UserBase(BaseModel):
    name: str
    email: str
    birthDate: date
    login: str

    @field_validator('birthDate')
    @classmethod
    def validar_maioridade(cls, v: date):
        hoje = date.today()
        # Calcula a idade
        idade = hoje.year - v.year - ((hoje.month, hoje.day) < (v.month, v.day))
        if idade < 18:
            raise ValueError("O usuário deve ter pelo menos 18 anos para se cadastrar.")
        return v

# Como a senha não está no UserBase, ela não vai vazar nos outros endpoints
class UserCreate(UserBase):
    cpf: str
    password: str

    @field_validator('cpf')
    @classmethod
    def validar_cpf(cls, v: str):
        # Remove pontos e traços
        cpf_limpo = re.sub(r'[^0-9]', '', v)
        if len(cpf_limpo) != 11:
            # Se disparar um ValueError, o FastAPI automaticamente bloqueia a requisição e retorna erro para o cliente
            raise ValueError("O CPF deve conter exatamente 11 dígitos numéricos.")
        return cpf_limpo

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    password: str | None = None
    # TODO: colocar os outros atributos
    
class UserBetSummary(BaseModel):
    id: int
    points: Decimal
    prediction: str
    status: str
    multiplier: Decimal
    user_id: int
    game: GameResponse

# No Response, tiramos a senha, mas adicionamos os dados gerados pelo sistema
class UserResponse(UserBase):
    id: int
    isAdmin: bool
    isActive: bool
    points: float
    max_points: float
    right_calls: int
    bets: list[UserBetSummary] = []

    model_config = ConfigDict(from_attributes=True)