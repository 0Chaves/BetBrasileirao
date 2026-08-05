from sqlalchemy.orm import Session
from models.bet_model import Bet
import schemas.bet_schema as schema

def get_bet(db: Session, bet_id: int):
    return db.query(Bet).filter(Bet.id == bet_id).first()

def get_bets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Bet).offset(skip).limit(limit).all()

def create_bet(db: Session, bet: schema.BetCreate):
    db_bet = Bet(**bet.model_dump())
    db.add(db_bet)
    db.commit()
    db.refresh(db_bet)  # Atualiza o objeto com o ID gerado pelo banco
    return db_bet

def update_bet(db: Session, bet_id: int, bet_update: schema.BetUpdate):
    db_bet = get_bet(db, bet_id)
    if not db_bet:
        return None
    
    # Extrai os dados enviados e atualiza apenas os campos fornecidos (o model_dump traz um dicionario com os atributos)
    update_data = bet_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_bet, key, value)
        
    db.commit()
    db.refresh(db_bet)
    return db_bet

def delete_bet(db: Session, bet_id: int):
    db_bet = get_bet(db, bet_id)
    if not db_bet:
        return None
    db.delete(db_bet)
    db.commit()
    return db_bet