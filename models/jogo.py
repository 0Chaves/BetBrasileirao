from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Jogo:
    status: str
    idTimeA: int
    idTimeB: int
    apostadoresTimeA: int
    apostadoresTimeB: int
    timeVencedor: int
    golsTimeA: int
    golsTimeB: int
    id: int = None