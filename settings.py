"""Настройки приложения Укоротителя ссылок."""
import os


class Config(object):
    """Настройки приложения Укоротителя ссылок."""

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
