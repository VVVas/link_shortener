"""Обработчик ошибок Укоротителя ссылок."""
from http import HTTPStatus

from flask import jsonify, render_template

from . import app, db


class InvalidAPIUsageError(Exception):
    """Класс ошибок API."""

    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        """Инициализация объекта ошибки API."""
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        """Формирование словаря с сообщение об ошибке."""
        return dict(message=self.message)


@app.errorhandler(InvalidAPIUsageError)
def invalid_api_usage(error):
    """Обработка ошибок API."""
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    """Обработка ошибки 404."""
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    """Обработка ошибки 500."""
    db.session.rollback()
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
