"""Модели Укоротителя ссылок."""
from datetime import datetime, timezone

from . import db


def aware_utcnow():
    """datetime.utcnow deprecated."""

    return datetime.now(timezone.utc)


class URLMap(db.Model):
    """Модель Укоротителя ссылок."""

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    # timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    timestamp = db.Column(db.DateTime, default=aware_utcnow)
