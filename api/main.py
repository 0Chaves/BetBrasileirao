from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine
from core.config import settings

# Import das Controllers (Routers)
from controllers import team_controller, user_controller, game_controller, bet_controller, auth_controller

# Cria as tabelas na inicialização
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Api do Bet Brasileirão")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra os controllers na aplicação principal para o fastapi descobrir as rotas
app.include_router(auth_controller.router)
app.include_router(team_controller.router)
app.include_router(user_controller.router)
app.include_router(game_controller.router)
app.include_router(bet_controller.router)
