# Orders List
Приложение позволяет просматривать заказы клиентов, стоимость и дату поставки в браузере

## Фишки приложения
- Автоматическое обновление данных из Google таблицы
- Просмотр заказов в браузере с подгрузкой дополнительных данных по кнопке
- Отображение общего числа заказов, их суммы и статистики по дням

## Используемые технологии

- [Flask] -  Фреймворк для создания веб-приложений на языке программирования Python
- [PostgreSQL] - Система управления базами данных
- [React] - JavaScript-библиотека для создания пользовательских интерфейсов

## Запуск

### База данных
Установите PostgreSQL c [официального сайта](https://www.postgresql.org/download/)
Запустите pgAdmin4

### Сервер
Установите Python 3.6 и выше c [официального сайта](https://www.python.org/downloads/)
Установите зависимости сервера (Необходимо находиться в директории проекта):
```
cd ./backend
pip install -r requirements.txt
```
Укажите в файле `backend/config.py` обязательные значения:
- `DB_PATH` - Путь или адрес [базы данных](#База-данных)
- `SERVER_HOST` - Адрес хоста приложения (По умолчанию '127.0.0.1')
- `SERVER_PORT` - Порт приложения (По умолчанию 5000)
- `GOOGLE_SHEETS_SERVICE_ACCOUNT_KEY` - Относительный путь к файлу с ключами Google API
- `GOOGLE_SHEETS` - Ссылка на таблицу Google Sheets

Запустите сервер:
```
python run.py
```

API доступно по адресу

### Клиент
Установите NodeJS 16.16.0 и выше c [официального сайта](https://nodejs.org/en/)
Установите зависимости клиента (Необходимо находиться в директории проекта):
```
cd ./frontend
npm install
```
Укажите в файле `backend/config.py` обязательные значения:
- `API_SERVER` - Ссылка на сервер (По умолчанию 'http://localhost:5000/')

Запустите клиент:
```
npm start
```

Клиент доступен для открытия на локальной машине по адресу 'http://localhost:3000'

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Flask]: <https://flask.palletsprojects.com/en/2.1.x/>
   [PostgreSQL]: <https://www.postgresql.org/>
   [React]: <https://ru.reactjs.org/>
