from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    JWT_SECRET: str = "secret-key-123"  # use dotenv in real apps


settings = Settings()
