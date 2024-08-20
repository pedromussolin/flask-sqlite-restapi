import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'admin'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
