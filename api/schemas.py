#TODO: revisar validações
from pydantic import BaseModel, ConfigDict, field_validator
from datetime import date
import re
from decimal import Decimal

# ==============
# ==== TEAM ====
# ==============

# Atributos compartilhados tanto na criação quanto na visualização
class TeamBase(BaseModel):
    name: str
    flag: str
    code: str
    group: str
    wins: int = 0
    losses: int = 0
    draws: int = 0
    
# Schema para validação ao CRIAR um projeto (entrada do POST)
class TeamCreate(TeamBase):
    pass

# Schema para validação ao ATUALIZAR um projeto (entrada do PUT)
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

# Schema para RETORNAR um projeto (saída das rotas)
class TeamResponse(TeamBase):
    id: int

    # O SQLAlchemy preenche essas listas automaticamente através dos 'relationships'
    games_as_team_a: list[GameSummary] = []
    games_as_team_b: list[GameSummary] = []
    won_games: list[GameSummary] = []
    model_config = ConfigDict(from_attributes=True)

# ==============
# ==== USER ====
# ==============

class UserBase(BaseModel):
    name: str
    email: str
    cpf: str
    birthDate: date
    login: str
    
    @field_validator('cpf')
    @classmethod
    def validar_cpf(cls, v: str):
        # Remove pontos e traços
        cpf_limpo = re.sub(r'[^0-9]', '', v)
        if len(cpf_limpo) != 11:
            # Se disparar um ValueError, o FastAPI automaticamente bloqueia a requisição e retorna erro para o cliente
            raise ValueError("O CPF deve conter exatamente 11 dígitos numéricos.")
        return cpf_limpo

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
    senha: str

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    senha: str | None = None
    # TODO: colocar os outros atributos
    
class UserBetSummary(BaseModel):
    id: int
    points: Decimal
    prediction: str
    status: str
    multiplier: Decimal
    user_id: int
    game: GameResponse
class BetSummary(BaseModel):
    id: int
    points: Decimal
    prediction: str
    status: str
    multiplier: Decimal
    user_id: int

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

# ==============
# ==== GAME ====
# ==============
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

# =============
# ==== BET ====
# =============

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