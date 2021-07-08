"""
    :author: Edgard Oliveira
    :source: https://raw.githubusercontent.com/greyli/catchat/master/catchat/settings.py
"""

import os
import sys

from enum import Enum, auto


class Database(Enum):
    POSTGRESQL = auto()
    ORACLE = auto()
    SQLITE = auto()

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'I am the bone of my sword!')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', "postgresql://postgres:postgres@localhost:5432/emcobranca")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BABEL_DEFAULT_LOCALE = 'br'

class DevelopmentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}