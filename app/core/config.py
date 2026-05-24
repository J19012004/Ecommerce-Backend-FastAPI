from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Ecommerce API"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    DATABASE_URL: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    REDIS_URL: str

    class Config:
        env_file = ".env"


settings = Settings()