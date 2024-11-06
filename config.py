import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:mar211998@127.0.0.1/:5432/finnisample")
    SQLALCHEMY_TRACK_MODIFICATIONS = False