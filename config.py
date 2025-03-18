from dotenv import load_dotenv
import os

class Config():
    load_dotenv()
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    SQLALCHEMY_DATABASE_URI = os.getenv("Database_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
