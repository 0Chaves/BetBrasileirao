from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from core.config import settings
engine = create_engine(settings.database_url, pool_pre_ping=True)   # pool_pre_ping verifica se a conexão ainda é válida antes de enviar comandos

# Cria a fábrica de sessões para o PostgreSQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para a criação dos modelos
class Base(DeclarativeBase):
    pass