# config.py

import os

class Config:
    # Application settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 5000

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Data settings
    DATA_DIRECTORY = 'data'
    DATA_FILE_FORMAT = 'csv'

    # Optimization settings
    OPTIMIZATION_ALGORITHM = 'genetic_algorithm'
    OPTIMIZATION_POPULATION_SIZE = 100
    OPTIMIZATION_GENERATIONS = 50
    OPTIMIZATION_MUTATION_RATE = 0.1

    # AI settings
    AI_MODEL_DIRECTORY = 'ai_models'
    AI_MODEL_FILE_FORMAT = 'pkl'

    # API settings
    API_VERSION = 'v1'
    API_PREFIX = f'/api/{API_VERSION}'

    # Logging settings
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'app.log'

    # Email notification settings
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USERNAME = 'your-email@example.com'
    SMTP_PASSWORD = 'your-email-password'
    ADMIN_EMAIL = 'admin@example.com'

    # Celery settings (if using Celery for background tasks)
    CELERY_BROKER_URL = 'redis://localhost:6379'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev_database.db'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_database.db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}