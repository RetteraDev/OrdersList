"""Начальные настройки базы данных и сервера"""
__author__ = 'RetteraDev'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_PATH, DB_TRACK_MODIFICATIONS

# Запуск сервера
app = Flask(__name__)

# Конфигурация базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DB_TRACK_MODIFICATIONS
db = SQLAlchemy(app)

# Подключим модели таблиц из базы и создадим их
import models.orders
db.create_all()

# Подключим EndPoints для запросов
import views

# Подключим события по расписанию
import shedulers
