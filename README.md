# «Укротитель ссылок» — сайт, который создаёт короткие ссылки из длинных.
Реализован веб-интерфейс и API для работы с внешними сервисами.

## Как развернуть  

Создать окружение  
```  
python -m venv venv  
```  

Активировать окружение, обновить pip и установить зависимости  
```  
source venv/Scripts/activate  
python -m pip install --upgrade pip  
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

По окончании использования деактивировать окружение  
```  
deactivate  
```  

## Стек технологий  
Python, Flask, SQLAlchemy, SQLite  

[Мишустин Василий](https://github.com/vvvas), v@vvvas.ru  
