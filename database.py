from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = "postgresql+psycopg2://postgres:senha123@localhost:5433/db_apostas"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)   # pool_pre_ping verifica se a conexão ainda é válida antes de enviar comandos

# Cria a fábrica de sessões para o PostgreSQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para a criação dos modelos
class Base(DeclarativeBase):
    pass