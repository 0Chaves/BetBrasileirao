from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg2://postgres:senha123@localhost:5433/db_apostas"

    secret_key: str = "14f3a2a55971b1447bd0ab7ee67e7fa690bce8eeeda42f9c971f86170202b566" #.env sobrescreve a key padrao
    algorithm: str = "HS256"
    access_token_expire_hours: int = 24

    frontend_origin: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
