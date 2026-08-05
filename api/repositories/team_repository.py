from sqlalchemy.orm import Session
from models.team_model import Team
import schemas.team_schema as schema

def get_team(db: Session, team_id: int):
    return db.query(Team).filter(Team.id == team_id).first()

def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Team).offset(skip).limit(limit).all()

def create_team(db: Session, team: schema.TeamCreate):
    db_team = Team(**team.model_dump())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)  # Atualiza o objeto com o ID gerado pelo banco
    return db_team

def update_team(db: Session, team_id: int, team_update: schema.TeamUpdate):
    db_team = get_team(db, team_id)
    if not db_team:
        return None
    
    # Extrai os dados enviados e atualiza apenas os campos fornecidos (o model_dump traz um dicionario com os atributos)
    update_data = team_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_team, key, value)
        
    db.commit()
    db.refresh(db_team)
    return db_team

def delete_team(db: Session, team_id: int):
    db_team = get_team(db, team_id)
    if not db_team:
        return None
    db.delete(db_team)
    db.commit()
    return db_team
