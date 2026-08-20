from sqlalchemy.orm import Session
from models.user_model import User
import schemas.user_schema as schema
from decimal import Decimal
from repositories.base_repository import BaseRepository
from sqlalchemy import or_
from core.security import hash_password

class UserRepository(BaseRepository[User, schema.UserCreate, schema.UserUpdate]):

    def save(self, db: Session, object: schema.UserCreate) -> User:
        data = object.model_dump()
        data["password"] = hash_password(data["password"])
        db_object = self.model(**data)
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        return db_object

    # Busca por email OU login — será usada no /auth/login e para checar duplicidade no cadastro
    def find_by_identifier(self, db: Session, identifier: str) -> User | None:
        return (
            db.query(User)
            .filter(or_(User.email == identifier, User.login == identifier))
            .first()
        )
    
    def find_ranking_by_points(self, db: Session, skip: int = 0, limit: int = 100) -> list[User]:
        return (
            db.query(User)
            .order_by(User.points.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def find_ranking_by_right_calls(self, db: Session, skip: int = 0, limit: int = 100) -> list[User]:
        return (
            db.query(User)
            .order_by(User.right_calls.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def deactivate_user(self, db: Session, user_id: int) -> User | None:
        db_user = self.findById(db, user_id)
        if not db_user:
            return None

        db_user.isActive = False
        db.commit()
        db.refresh(db_user)
        return db_user

    def atualizar_pontos_usuario(self, db: Session, user_id: int, pontos_para_adicionar: Decimal) -> User | None:
        db_user = self.findById(db, user_id)
        if not db_user:
            return None
            
        novo_saldo = db_user.points + pontos_para_adicionar
        if novo_saldo < 0:
            raise ValueError("Saldo insuficiente para a operação.")
            
        db_user.points = novo_saldo
        if novo_saldo > db_user.max_points:
            db_user.max_points = novo_saldo
            
        db.commit()
        db.refresh(db_user)
        return db_user

user_repository = UserRepository(User)