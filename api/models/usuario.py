from dataclasses import dataclass
from datetime import date

@dataclass(slots=True, frozen=True)
class Usuario:
    isAdmin: bool
    statusAtivo: bool
    nome: str
    email: str
    cpf: str
    dataNascimento: date
    login: str
    senha: str
    pontos: float
    pontos_maximo: float
    totalAcertos: int
    id: int = None