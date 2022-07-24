"""Запуск сервера"""
__author__ = 'RetteraDev'

from app import app
from config import SERVER_HOST, SERVER_PORT, SERVER_DEBUG


app.run(
    host=SERVER_HOST,
    post=SERVER_PORT,
    debug=SERVER_DEBUG
)
