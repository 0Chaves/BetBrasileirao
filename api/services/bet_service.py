from decimal import Decimal, ROUND_HALF_UP
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.user_model import User
from models.bet_model import Bet
import schemas.bet_schema as schema
from repositories.user_repository import user_repository
from repositories.game_repository import game_repository
from collections import Counter

class BetService:
    def __init__(self, db: Session):
        self.db = db

    def place_bet(self, bet_in: schema.BetCreate, current_user: User) -> Bet:
        if bet_in.points > current_user.points:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Saldo insuficiente para esta aposta",
            )

        user_repository.atualizar_pontos_usuario(self.db, current_user.id, -bet_in.points)

        game_bets = game_repository.findById(db=self.db, id=bet_in.game_id).bets
        bets_by_prediction = Counter(bet.prediction for bet in game_bets)

        total_bets = len(game_bets)
        bets_on_prediction = bets_by_prediction[bet_in.prediction]

        multiplier = (
            Decimal(total_bets + 2) / Decimal(bets_on_prediction + 1)
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        # persiste a aposta
        db_bet = Bet(
            points=bet_in.points,
            prediction=bet_in.prediction,
            status="em_andamento",
            multiplier=multiplier,
            user_id=current_user.id,
            game_id=bet_in.game_id,
        )
        self.db.add(db_bet)
        self.db.commit()
        self.db.refresh(db_bet)
        return db_bet