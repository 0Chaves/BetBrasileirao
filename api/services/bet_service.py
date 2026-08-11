from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.user_model import User
from models.bet_model import Bet
import schemas.bet_schema as schema
from repositories.user_repository import user_repository


class BetService:
    def __init__(self, db: Session):
        self.db = db

    def place_bet(self, bet_in: schema.BetCreate, current_user: User) -> Bet:
        if bet_in.points > current_user.points:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Saldo insuficiente para esta aposta",
            )

        # Debita o saldo do usuário autenticado (nunca de um user_id arbitrário)
        user_repository.atualizar_pontos_usuario(self.db, current_user.id, -bet_in.points)

        # persiste a aposta
        db_bet = Bet(
            points=bet_in.points,
            prediction=bet_in.prediction,
            status="em_andamento",
            multiplier=bet_in.multiplier,
            user_id=current_user.id,
            game_id=bet_in.game_id,
        )
        self.db.add(db_bet)
        self.db.commit()
        self.db.refresh(db_bet)
        return db_bet