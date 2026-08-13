from models.team_model import Team
import schemas.team_schema as schema
from repositories.base_repository import BaseRepository
from sqlalchemy.orm import Session

class TeamRepository(BaseRepository[Team, schema.TeamCreate, schema.TeamUpdate]):

    def findByName(self, db: Session, name: str, ):
        return db.query(self.model).filter(self.model.name == name).first()

team_repository = TeamRepository(Team)