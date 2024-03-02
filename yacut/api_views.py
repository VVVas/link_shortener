"""API Укоротителя ссылок."""
import re
from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .constants import CUSTOM_ID_PATTERN, ORIGINAL_MAX, SHORT_ID_MAX
from .error_handlers import InvalidAPIUsageError
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    """Создание корокой ссылки."""
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsageError('Отсутствует тело запроса')
    if 'url' not in data or not data['url']:
        raise InvalidAPIUsageError('"url" является обязательным полем!')
    if len(data['url']) > ORIGINAL_MAX:
        raise InvalidAPIUsageError('Указано недопустимое имя для ссылки')
    if 'custom_id' not in data or not data['custom_id']:
        data['custom_id'] = get_unique_short_id()
    if URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsageError(
            'Предложенный вариант короткой ссылки уже существует.'
        )
    if (
        len(data['custom_id']) > SHORT_ID_MAX or
        not re.match(CUSTOM_ID_PATTERN, data['custom_id'])
    ):
        raise InvalidAPIUsageError('Указано недопустимое имя для короткой ссылки')
    urlmap = URLMap(
        original=data['url'],
        short=data['custom_id']
    )
    db.session.add(urlmap)
    db.session.commit()
    return jsonify({
        'url': urlmap.original,
        'short_link': request.host_url + urlmap.short
    }), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_urlmap(short_id):
    """Получение оригинальной ссылки из короткой."""
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsageError('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': urlmap.original}), HTTPStatus.OK
