from decimal import Decimal
from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship  
from database import Base

class Bet(Base):
    __tablename__ = "bets"

    id: Mapped[int] = mapped_column(primary_key = True, index = True)
    points: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)
    prediction: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(255), nullable=False) #em andamento, finalizada
    multiplier: Mapped[Decimal] = mapped_column(Numeric(10,2), nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="bets", foreign_keys=[user_id])

    game_id: Mapped[int] = mapped_column(ForeignKey("games.id"), nullable=False)
    game: Mapped["Game"] = relationship(back_populates="bets", foreign_keys=[game_id])