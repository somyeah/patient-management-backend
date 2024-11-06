import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:mar211998@localhost:5432/finnisample")
    SQLALCHEMY_TRACK_MODIFICATIONS = False