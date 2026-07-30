from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
import crud
from database import SessionLocal, engine

# Cria as tabelas na inicialização
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Api do Aposta Copa")

# Abre uma sessão do banco e fecha após a requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ROTAS DO CRUD ---

@app.post("/teams/", response_model=schemas.TeamResponse, status_code=status.HTTP_201_CREATED)
def criar_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db=db, team=team)

@app.get("/teams/", response_model=list[schemas.TeamResponse])
def listar_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_teams(db=db, skip=skip, limit=limit)

@app.get("/teams/{team_id}", response_model=schemas.TeamResponse)
def obter_team(team_id: int, db: Session = Depends(get_db)):
    db_team = crud.get_team(db=db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Time não encontrado")
    return db_team

@app.put("/teams/{team_id}", response_model=schemas.TeamResponse)
def atualizar_team(team_id: int, team_update: schemas.TeamUpdate, db: Session = Depends(get_db)):
    db_team = crud.update_team(db=db, team_id=team_id, team_update=team_update)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Time não encontrado")
    return db_team

@app.delete("/teams/{team_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_team(team_id: int, db: Session = Depends(get_db)):
    db_team = crud.delete_team(db=db, team_id=team_id)
    if db_team is None:
        raise HTTPException(status_code=404, detail="Time não encontrado")
    return None

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id,     "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return{"item_name": item.name, "item_id": item_id}


