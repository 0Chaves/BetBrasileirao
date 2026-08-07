from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas.bet_schema as schema
from repositories import bet_repository


# Equivalente ao @RestController e @RequestMapping("/bets") do Spring
router = APIRouter(
    prefix="/bets",
    tags=["Bets"] # Isso agrupa os endpoints bonitinho na documentação do Swagger
)

# Dependência do banco de dados (pode ser movida para um arquivo utils.py no futuro)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.BetResponse, status_code=status.HTTP_201_CREATED)
def criar_bet(bet: schema.BetCreate, db: Session = Depends(get_db)):
    return bet_repository.create_bet(db=db, bet=bet)

@router.get("/", response_model=list[schema.BetResponse])
def listar_bets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return bet_repository.get_bets(db=db, skip=skip, limit=limit)

@router.get("/{bet_id}", response_model=schema.BetResponse, status_code=status.HTTP_200_OK)
def obter_bet(bet_id: int, db: Session = Depends(get_db)):
    db_bet = bet_repository.get_bet(db=db, bet_id=bet_id)
    if db_bet is None:
        raise HTTPException(status_code=404, detail="Aposta não encontrado")
    return db_bet

@router.put("/{bet_id}", response_model=schema.BetResponse, status_code=status.HTTP_200_OK)
def atualizar_bet(bet_id: int, bet_update: schema.BetUpdate, db: Session = Depends(get_db)):
    db_bet = bet_repository.update_bet(db=db, bet_id=bet_id, bet_update=bet_update)
    if db_bet is None:
        raise HTTPException(status_code=404, detail="Aposta não encontrado")
    return db_bet

@router.delete("/{bet_id}", status_code=status.HTTP_200_OK)
def deletar_bet(bet_id: int, db: Session = Depends(get_db)):
    db_bet = bet_repository.delete_bet(db=db, bet_id=bet_id)
    if db_bet is None:
        raise HTTPException(status_code=404, detail="Aposta não encontrado")
    return None