from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models
import schemas
import crud
from database import SessionLocal, engine

# Cria as tabelas na inicialização (ideal apenas para desenvolvimento/testes rápidos)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Api do Aposta Copa")

# Dependência que abre uma sessão do banco e garante que ela seja fechada após a requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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


