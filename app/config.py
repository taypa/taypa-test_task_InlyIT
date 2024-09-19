import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / "app/config.env"
load_dotenv(dotenv_path=env_path)

class Settings:
    __DB_HOST: str = os.getenv("DB_HOST")
    __DB_PORT: int= os.getenv("DB_PORT", 5432)
    __DB_NAME: str= os.getenv("DB_NAME")
    __DB_USER: str= os.getenv("DB_USER")
    __DB_PASSWORD: str= os.getenv("DB_PASSWORD")

    URL = (f"postgresql://{__DB_USER}:{__DB_PASSWORD}@"
            f"{__DB_HOST}:{__DB_PORT}/{__DB_NAME}")
