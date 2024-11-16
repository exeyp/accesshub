import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'f7d7c511fd467783aec43f6cfc994361')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    # Включится только отладочный режим без автоперезагрузки.
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhos:5432/accesshub_db'
