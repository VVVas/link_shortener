# YaCut — Укоротитель ссылок.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone  
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv  
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Создать и заполнить файл .env по примеру .env.example

Создать таблицы в БД

```
flask db upgrade
```

Запустить

```
flask run
```
