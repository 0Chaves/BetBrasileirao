from models.bet_model import Bet
import schemas.bet_schema as schema
from repositories.base_repository import BaseRepository

class BetRepository(BaseRepository[Bet, schema.BetCreate, schema.BetUpdate]):
    pass

bet_repository = BetRepository(Bet)