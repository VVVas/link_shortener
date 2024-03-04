"""Обработка запросов к Укоротителю ссылок."""
import logging
from http import HTTPStatus
from random import choice

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .constants import (SHORT_ID_ATTEMPTS_NUMBER, SHORT_ID_LENGHT,
                        SHORT_ID_SYMBOLS)
from .forms import URLMapForm
from .models import URLMap


def get_unique_short_id():
    """Получение уникальной короткой ссылки."""
    short_id = ''
    counter = 0
    while URLMap.query.filter_by(short=short_id).first() or not short_id:
        short_id = (''.join(
            [choice(SHORT_ID_SYMBOLS) for x in range(SHORT_ID_LENGHT)]
        ))
        if counter == SHORT_ID_ATTEMPTS_NUMBER:
            logging.error(
                f'Число попыток генерации короткой ссылки {counter}. '
                'Возможно осталось мало свободных коротких ссылок. ',
                stack_info=True
            )
        if counter > (SHORT_ID_ATTEMPTS_NUMBER * SHORT_ID_LENGHT):
            logging.critical(
                f'Число попыток генерации короткой ссылки {counter}. '
                'Возможно осталось мало свободных коротких ссылок. '
                'Пользователь получил сообщение об ошибке 500.',
                stack_info=True
            )
            abort(HTTPStatus.INTERNAL_SERVER_ERROR)
        counter += 1
    return short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Главная страница с формой создание короткой ссылки."""
    form = URLMapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        elif URLMap.query.filter_by(short=custom_id).first():
            flash('Предложенный вариант короткой ссылки уже существует.',
                  'duplicate')
            return render_template('index.html', form=form)
        urlmap = URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        db.session.add(urlmap)
        db.session.commit()
        flash(url_for('redirect_view', short_id=urlmap.short, _external=True),
              'url')
    return render_template('index.html', form=form)


@app.route('/<string:short_id>')
def redirect_view(short_id):
    """Перенаправление из короткой ссылки и оригинальную."""
    urlmap = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(urlmap.original)
