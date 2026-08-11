from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from core.dependencies import get_db, get_current_admin_user
from models.user_model import User
import schemas.team_schema as schema
from repositories.team_repository import team_repository

# Equivalente ao @RestController e @RequestMapping("/teams") do Spring
router = APIRouter(
    prefix="/teams",
    tags=["Teams"]
)


@router.post("/", response_model=schema.TeamResponse, status_code=status.HTTP_201_CREATED)
def criar_team(team: schema.TeamCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    return team_repository.save(db=db, object=team)

@router.get("/", response_model=list[schema.TeamResponse])
def listar_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return team_repository.findAll(db=db, skip=skip, limit=limit)

@router.get("/{team_id}", response_model=schema.TeamResponse, status_code=status.HTTP_200_OK)
def obter_team(team_id: int, db: Session = Depends(get_db)):
    db_team = team_repository.findById(db=db, id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Time não encontrado")
    return db_team

@router.put("/{team_id}", response_model=schema.TeamResponse, status_code=status.HTTP_200_OK)
def atualizar_team(team_id: int, team_update: schema.TeamUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_team = team_repository.update(db=db, id=team_id, obj_update=team_update)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Time não encontrado")
    return db_team

@router.delete("/{team_id}", status_code=status.HTTP_200_OK)
def deletar_team(team_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_team = team_repository.delete(db=db, id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Time não encontrado")
    return None