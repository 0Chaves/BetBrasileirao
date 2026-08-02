from fastapi import FastAPI
import models
from database import engine

# Import das Controllers (Routers)
from controllers import team_controller, user_controller, game_controller

# Cria as tabelas na inicialização
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Api do Aposta Copa")

# Registra os controllers na aplicação principal para o fastapi descobrir as rotas
app.include_router(team_controller.router)
app.include_router(user_controller.router)
app.include_router(game_controller.router)

@app.get("/")
def read_root():
    return {"Hello": "Bem-vindo a API do Aposta Copa!"}
