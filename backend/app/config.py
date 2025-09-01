import os
from dotenv import load_dotenv

# load eviornment vairables from .env
load_dotenv()

class Settings:
    def __init__(self):
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_PORT")
        self.DB_NAME = os.getenv("DB_NAME")

        self.JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    @property
    def DATABASE_URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"