from pydantic import BaseModel, ConfigDict

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
    vitorias: int = 0
    derrotas: int = 0
    empates: int = 0

# Schema para RETORNAR um projeto (saída das rotas)
class TeamResponse(TeamBase):
    id: int
    # Configuração do Pydantic v2 para ler objetos do ORM (SQLAlchemy)
    model_config = ConfigDict(from_attributes=True)