from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from core.dependencies import get_db, get_current_admin_user
from models.user_model import User
import schemas.game_schema as schema
from repositories.game_repository import game_repository

# Equivalente ao @RestController e @RequestMapping("/games") do Spring
router = APIRouter(
    prefix="/games",
    tags=["Games"]
)


@router.post("/", response_model=schema.GameResponse, status_code=status.HTTP_201_CREATED)
def criar_game(game: schema.GameCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return game_repository.save(db=db, object=game)

# Listagem é pública (tela de jogos)
@router.get("/", response_model=list[schema.GameResponse])
def listar_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return game_repository.findAll(db=db, skip=skip, limit=limit)

@router.get("/{game_id}", response_model=schema.GameResponse, status_code=status.HTTP_200_OK)
def obter_game(game_id: int, db: Session = Depends(get_db)):
    db_game = game_repository.findById(db=db, id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return db_game

# Atualização de placar/status/vencedor é operação administrativa
@router.put("/{game_id}", response_model=schema.GameResponse, status_code=status.HTTP_200_OK)
def atualizar_game(game_id: int, game_update: schema.GameUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_game = game_repository.update(db=db, id=game_id, obj_update=game_update)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return db_game

@router.delete("/{game_id}", status_code=status.HTTP_200_OK)
def deletar_game(game_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_game = game_repository.delete(db=db, id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return None