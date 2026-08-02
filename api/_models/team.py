from dataclasses import dataclass

@dataclass(slots=True)
class Team:
    nome: str
    bandeira: str
    sigla: str
    grupo: str
    vitorias: int = 0
    derrotas: int = 0
    empates: int = 0
    id: int = None