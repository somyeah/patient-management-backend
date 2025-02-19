import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:*****@localhost:5432/finnisample")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
