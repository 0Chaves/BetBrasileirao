from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from core.dependencies import get_db, get_current_user, get_current_admin_user
from models.user_model import User
import schemas.bet_schema as schema
from repositories.bet_repository import bet_repository
from services.bet_service import BetService

# Equivalente ao @RestController e @RequestMapping("/bets") do Spring
router = APIRouter(
    prefix="/bets",
    tags=["Bets"]
)


# A aposta é sempre criada em nome do usuário autenticado
@router.post("/", response_model=schema.BetResponse, status_code=status.HTTP_201_CREATED)
def criar_bet(bet: schema.BetCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return BetService(db).place_bet(bet, current_user)

@router.get("/me", response_model=list[schema.BetResponse])
def minhas_bets(current_user: User = Depends(get_current_user)):
    return current_user.bets

@router.get("/", response_model=list[schema.BetResponse])
def listar_bets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return bet_repository.findAll(db=db, skip=skip, limit=limit)

@router.get("/{bet_id}", response_model=schema.BetResponse, status_code=status.HTTP_200_OK)
def obter_bet(bet_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_bet = bet_repository.findById(db=db, id=bet_id)
    if db_bet is None:
        raise HTTPException(status_code=404, detail="Aposta não encontrada")
    if db_bet.user_id != current_user.id and not current_user.isAdmin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Você não tem permissão para ver esta aposta")
    return db_bet

@router.put("/{bet_id}", response_model=schema.BetResponse, status_code=status.HTTP_200_OK)
def atualizar_bet(bet_id: int, bet_update: schema.BetUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_bet = bet_repository.update(db=db, id=bet_id, obj_update=bet_update)
    if db_bet is None:
        raise HTTPException(status_code=404, detail="Aposta não encontrada")
    return db_bet

@router.delete("/{bet_id}", status_code=status.HTTP_200_OK)
def deletar_bet(bet_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_bet = bet_repository.delete(db=db, id=bet_id)
    if db_bet is None:
        raise HTTPException(status_code=404, detail="Aposta não encontrada")
    return None