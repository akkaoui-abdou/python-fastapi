from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    """
    BaseSettings, from Pydantic, validates the data so that when we create an instance of Settings,
    environment and testing will have types of str and bool, respectively.
    Parameters:
    Returns:
    instance of Settings
    """
    PYTHONDONTWRITEBYTECODE: str
    PYTHONUNBUFFERED: str

    ENVIRONMENT: str
    TESTING: str
    UP: str
    DOWN: str
    WEB_SERVER: str

    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_USER: str
    MONGO_PASS: str
    MONGO_DB: str
    MONGO_COLLECTION: str
    MONGO_TEST_DB: str
    MONGO_URL: str


    class Config:
        env_file = './.env'


settings = Settings()