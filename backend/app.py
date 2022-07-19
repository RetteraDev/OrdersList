"""Начальные настройки базы данных и сервера"""
__author__ = 'RetteraDev'

from flask import Flask
from db.db_crud import init_db

# Выполнение операций по инициализации базы данных
init_db()

# Запуск сервера
app = Flask(__name__)

# Подключим EndPoints для запросов
import views

# Подключим события по расписанию
import shedulers
