from sqlalchemy.orm import Session
from models.user_model import User
import schemas.user_schema as schema
from decimal import Decimal
from repositories.base_repository import BaseRepository

class UserRepository(BaseRepository[User, schema.UserCreate, schema.UserUpdate]):
    
    def atualizar_pontos_usuario(self, db: Session, user_id: int, pontos_para_adicionar: Decimal) -> User | None:
        db_user = self.get(db, user_id)
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