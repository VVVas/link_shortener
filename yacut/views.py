from random import choice, shuffle

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap


# def get_unique_short_id(lenght=app.config['SHORT_ID_LENGHT']):
#     symbols = shuffle(list(app.config['SYMBOLS']))
#     print(''.join([choice(symbols) for x in range(lenght)]))
#     return ''.join([choice(symbols) for x in range(lenght)])

def get_unique_short_id(lenght=6):
    symbols = list('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    # print(''.join([choice(symbols) for x in range(lenght)]))
    return (''.join([choice(symbols) for x in range(lenght)]))


# def random_opinion():
#     quantity = Opinion.query.count()
#     if quantity:
#         offset_value = randrange(quantity)
#         opinion = Opinion.query.offset(offset_value).first()
#         return opinion

@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        # if URLMap.query.filter_by(original=original_link).first():
        #     flash('Такое мнение уже было оставлено ранее!')
        #     return render_template('add_opinion.html', form=form)
        custom_id = form.custom_id.data
        custom_id = get_unique_short_id()
        print(custom_id)
        if not custom_id:
            while URLMap.query.filter_by(short=custom_id).first():
                custom_id = get_unique_short_id()
        # if URLMap.query.filter_by(short=custom_id).first():
        #     flash('Предложенный вариант короткой ссылки уже существует.')
        #     return render_template('index.html', form=form)
        urlmap = URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        db.session.add(urlmap)
        db.session.commit()
        flash('Ваша новая ссылка готова')
    return render_template('index.html', form=form)

# @app.route('/')
# def index_view():
#     # quantity = Opinion.query.count()
#     # if not quantity:
#     #     abort(404)
#     # offset_value = randrange(quantity)
#     # opinion = Opinion.query.offset(offset_value).first()
#     # return render_template('opinion.html', opinion=opinion)
#     opinion = random_opinion()
#     if opinion is not None:
#         return render_template('opinion.html', opinion=opinion)
#     abort(404)


@app.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
    form = OpinionForm()
    if form.validate_on_submit():
        text = form.text.data
        if Opinion.query.filter_by(text=text).first():
            flash('Такое мнение уже было оставлено ранее!')
            return render_template('add_opinion.html', form=form)
        opinion = Opinion(
            title=form.title.data,
            text=form.text.data,
            source=form.source.data
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect(url_for('opinion_view', id=opinion.id))
    return render_template('add_opinion.html', form=form)


@app.route('/opinions/<int:id>')
def opinion_view(id):
    opinion = Opinion.query.get_or_404(id)
    return render_template('opinion.html', opinion=opinion)
