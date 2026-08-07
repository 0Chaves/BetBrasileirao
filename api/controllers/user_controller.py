from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas.user_schema as schema
from repositories.user_repository import user_repository


# Equivalente ao @RestController e @RequestMapping("/users") do Spring
router = APIRouter(
    prefix="/users",
    tags=["Users"] # Isso agrupa os endpoints bonitinho na documentação do Swagger
)

# Dependência do banco de dados (pode ser movida para um arquivo utils.py no futuro)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    return user_repository.save(db=db, user=user)

@router.get("/", response_model=list[schema.UserResponse])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return user_repository.findAll(db=db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=schema.UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_repository.findById(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return db_user

@router.put("/{user_id}", response_model=schema.UserResponse, status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_update: schema.UserUpdate, db: Session = Depends(get_db)):
    db_user = user_repository.update(db=db, user_id=user_id, user_update=user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return db_user

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_repository.delete(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    return None