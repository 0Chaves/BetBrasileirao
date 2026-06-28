from dataclasses import dataclass

@dataclass(slots=True)
class Team:
    nome: str
    vitorias: int
    derrotas: int
    empates: int
    id: int = None