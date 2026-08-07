from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas.game_schema as schema
from repositories.game_repository import game_repository


# Equivalente ao @RestController e @RequestMapping("/games") do Spring
router = APIRouter(
    prefix="/games",
    tags=["Games"] # Isso agrupa os endpoints bonitinho na documentação do Swagger
)

# Dependência do banco de dados (pode ser movida para um arquivo utils.py no futuro)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.GameResponse, status_code=status.HTTP_201_CREATED)
def criar_game(game: schema.GameCreate, db: Session = Depends(get_db)):
    return game_repository.save(db=db, game=game)

@router.get("/", response_model=list[schema.GameResponse])
def listar_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return game_repository.findAll(db=db, skip=skip, limit=limit)

@router.get("/{game_id}", response_model=schema.GameResponse, status_code=status.HTTP_200_OK)
def obter_game(game_id: int, db: Session = Depends(get_db)):
    db_game = game_repository.findById(db=db, game_id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return db_game

@router.put("/{game_id}", response_model=schema.GameResponse, status_code=status.HTTP_200_OK)
def atualizar_game(game_id: int, game_update: schema.GameUpdate, db: Session = Depends(get_db)):
    db_game = game_repository.update(db=db, game_id=game_id, game_update=game_update)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return db_game

@router.delete("/{game_id}", status_code=status.HTTP_200_OK)
def deletar_game(game_id: int, db: Session = Depends(get_db)):
    db_game = game_repository.delete(db=db, game_id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return None