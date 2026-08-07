from models.team_model import Team
import schemas.team_schema as schema
from repositories.base_repository import BaseRepository

class TeamRepository(BaseRepository[Team, schema.TeamCreate, schema.TeamUpdate]):
    pass

team_repository = TeamRepository(Team)