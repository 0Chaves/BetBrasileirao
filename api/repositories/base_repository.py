from sqlalchemy.orm import Session
from models.bet_model import Bet
import schemas.bet_schema as schema
from typing import Any, Generic, Type, TypeVar
from pydantic import BaseModel
from database import Base

# ModelType deve ser qualquer classe que herde do Base do SQLAlchemy
ModelType = TypeVar("ModelType", bound=Base)
# CreateSchemaType e UpdateSchemaType devem herdar do BaseModel do Pydantic
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        # Recebe a classe do modelo real (ex: Team, User) para que o SQLAlchemy saiba qual tabela consultar.
        self.model = model

    def findById(self, db: Session, id: Any) -> ModelType | None:
        return db.query(self.model).filter(self.model.id == id).first()

    def findAll(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()

    def save(self, db: Session, object: CreateSchemaType) -> ModelType:
        db_object = self.model(**object.model_dump())
        db.add(db_object)
        db.commit()
        db.refresh(db_object)  # Atualiza o objeto com o ID gerado pelo banco
        return db_object

    def update_bet(self, db: Session, id: Any, obj_update: UpdateSchemaType) -> ModelType | None:
        db_object = self.findById(db, id)
        if not db_object:
            return None
        
        # Extrai os dados enviados e atualiza apenas os campos fornecidos (o model_dump traz um dicionario com os atributos)
        update_data = obj_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_object, key, value)
            
        db.commit()
        db.refresh(db_object)
        return db_object

    def delete(self, db: Session, id: Any) -> ModelType | None:
        db_object = self.findById(db, id)
        if not db_object:
            return None
        db.delete(db_object)
        db.commit()
        return db_object