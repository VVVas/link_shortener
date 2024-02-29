from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, AnyOf, DataRequired, Length, Optional

from .constants import SHORT_ID_LENGHT, SYMBOLS_INPUT


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 256, message='Длина короткой ссылки должна быть от %(min)d до %(max)d символов.'),
                    URL(message='Не правильная длинная ссылка.')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(SHORT_ID_LENGHT, 16, message='Длина короткой ссылки должна быть от %(min)d до %(max)d символов.'),
                    AnyOf(values=SYMBOLS_INPUT, message='Используйте только следующие символы %(values)s.'),
                    Optional()]
    )
    submit = SubmitField('Создать')
