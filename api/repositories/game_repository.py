from models.game_model import Game
import schemas.game_schema as schema
from repositories.base_repository import BaseRepository

class GameRepository(BaseRepository[Game, schema.GameCreate, schema.GameUpdate]):
    pass

game_repository = GameRepository(Game)