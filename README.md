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
Укажите в файле `backend/config.py` значения:
`DB_PATH` - Путь или адрес [базы данных](#База-данных)
`GOOGLE_SHEETS_SERVICE_ACCOUNT_KEY` - Путь к файлу с ключами Google API
`GOOGLE_SHEETS` - Адрес таблицы Google Sheets

Запустите сервер:
```
python run.py
```

### Клиент
Установите NodeJS 16.16.0 и выше c [официального сайта](https://nodejs.org/en/)
```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```


## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## Лицензия
MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Flask]: <https://flask.palletsprojects.com/en/2.1.x/>
   [PostgreSQL]: <https://www.postgresql.org/>
   [React]: <https://ru.reactjs.org/>
