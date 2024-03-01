"""Форма для Укоротителя ссылок."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .constants import (CUSTOM_ID_PATTERN, ORIGINAL_MAX, SHORT_ID_MAX,
                        SHORT_ID_MIN)


class URLMapForm(FlaskForm):
    """Класс формы для Укоротителя ссылок."""

    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, ORIGINAL_MAX,
                   message=('Длина ссылки должна быть'
                            'от %(min)d до %(max)d символов.')),
            URL(message='Не правильная длинная ссылка.')
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(SHORT_ID_MIN, SHORT_ID_MAX,
                   message=('Длина короткой ссылки должна быть'
                            'от %(min)d до %(max)d символов.')),
            Regexp(regex=CUSTOM_ID_PATTERN,
                   message='Используйте только английские буквы и цифры.'),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
