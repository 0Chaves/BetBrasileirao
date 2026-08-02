from database import Base

# o . significa "nesta mesma pasta"
# esta importação é importante para o fastapi reconhecer as tabelas na criação
# o __init__ serve para transformar a pasta em package
from .team_model import Team
from .user_model import User
from .game_model import Game
from .bet_model import Bet