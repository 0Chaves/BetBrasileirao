from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.user_model import User
from models.game_model import Game
import schemas.game_schema as schema
from repositories.user_repository import user_repository
from repositories.game_repository import game_repository


class GameService:
    def __init__(self, db: Session):
            self.db = db

    def finalize_game(self, game_id: int) -> Game:
        db_game = game_repository.findById(db=self.db, id=game_id)
        if db_game is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Jogo não encontrado")

        if db_game.winner_str is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Jogo ainda não possui um resultado definido",
            )

        for bet in db_game.bets:
            if bet.status != "em_andamento":
                continue

            if bet.prediction == db_game.winner_str:
                premio = bet.points * bet.multiplier
                user_repository.atualizar_pontos_usuario(self.db, bet.user_id, premio)
                bet.user.right_calls += 1

            bet.status = "finalizada"

        # db_game.status = "FINISHED" #descomentar para atualizar os jogos de forma automatica junto das bets
        self.db.commit()
        self.db.refresh(db_game)
        return db_game