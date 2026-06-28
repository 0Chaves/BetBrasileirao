from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Aposta:
    pontos: float
    palpite: str
    status: str
    multiplicador: float
    idUsuario: int
    idJogo: int
    id: int = None