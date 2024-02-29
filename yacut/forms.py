from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .constants import SHORT_ID_LENGHT, CUSTOM_ID_PATTERN


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
                    Regexp(regex=CUSTOM_ID_PATTERN, message='Используйте только английские буквы и цифры.'),
                    Optional()]
    )
    submit = SubmitField('Создать')
