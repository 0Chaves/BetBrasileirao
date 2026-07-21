from sqlalchemy.orm import Session
import models
import schemas

def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()

def get_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Team).offset(skip).limit(limit).all()

def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(
        nome=team.nome,
        bandeira = team.bandeira,
        sigla = team.sigla,
        grupo = team.grupo,
        vitorias = team.vitorias,
        derrotas = team.derrotas,
        empates = team.empates,
    )
    db.add(db_team)
    db.commit()
    db.refresh(db_team)  # Atualiza o objeto com o ID gerado pelo banco
    return db_team

def update_team(db: Session, team_id: int, team_update: schemas.TeamUpdate):
    db_team = get_team(db, team_id)
    if not db_team:
        return None
    
    # Extrai os dados enviados e atualiza apenas os campos fornecidos
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