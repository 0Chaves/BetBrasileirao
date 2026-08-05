from sqlalchemy.orm import Session
from models.user_model import User
import schemas.user_schema as schema
from decimal import Decimal

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schema.UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # Atualiza o objeto com o ID gerado pelo banco
    return db_user

def update_user(db: Session, user_id: int, user_update: schema.UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    
    # Extrai os dados enviados e atualiza apenas os campos fornecidos (o model_dump traz um dicionario com os atributos)
    update_data = user_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
        
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

# TODO: Levar este metodo para o service
def atualizar_pontos_usuario(db: Session, user_id: int, pontos_para_adicionar: Decimal):
    # 1. Busca o usuário no banco
    db_user = db.query(User).filter(User.id == user_id).first()
    
    if not db_user:
        return None
        
    # 2 Obs: Para diminuir pontos, basta passar um valor negativo na variável
    novo_saldo = db_user.points + pontos_para_adicionar
    
    # Validação: não pode ficar negativo
    if novo_saldo < 0:
        raise ValueError("Saldo insuficiente para a operação.")
        
    # 3. Atualiza o objeto ORM
    db_user.points = novo_saldo
    
    # Atualiza o max_points se o usuário bateu um novo recorde
    if novo_saldo > db_user.max_points:
        db_user.max_points = novo_saldo
        
    # 4. Salva no banco de dados
    db.commit()
    db.refresh(db_user)
    
    return db_user