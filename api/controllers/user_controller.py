from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from core.dependencies import get_db, get_current_user, get_current_admin_user
from core.security import hash_password
from models.user_model import User
import schemas.user_schema as schema
from repositories.user_repository import user_repository

# Equivalente ao @RestController e @RequestMapping("/users") do Spring
router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# Cadastro é público (não exige token) — mas bloqueia e-mail/login duplicado
@router.post("/", response_model=schema.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    if user_repository.find_by_identifier(db, user.email) or user_repository.find_by_identifier(db, user.login):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="E-mail ou login já cadastrado")
    return user_repository.save(db=db, object=user)


# Usado pelo frontend para restaurar a sessão a partir do token salvo.
@router.get("/me", response_model=schema.UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/", response_model=list[schema.UserResponse])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return user_repository.findAll(db=db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=schema.UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.id != user_id and not current_user.isAdmin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Você não tem permissão para ver este usuário")

    db_user = user_repository.findById(db=db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return db_user

@router.put("/{user_id}", response_model=schema.UserResponse, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_update: schema.UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.id != user_id and not current_user.isAdmin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Você não tem permissão para editar este usuário")

    if user_update.password:
        user_update.password = hash_password(user_update.password)

    db_user = user_repository.update(db=db, id=user_id, obj_update=user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return db_user

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_admin_user)):
    db_user = user_repository.delete(db=db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return None