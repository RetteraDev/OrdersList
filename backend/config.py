"""Константы деплоя проекта"""
__author__ = 'RetteraDev'

import os

DB_PATH = "postgresql://postgres:1@localhost:5432"
DB_TRACK_MODIFICATIONS = True

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000
SERVER_DEBUG = False

GOOGLE_SHEETS_SERVICE_ACCOUNT_KEY = "service_account.json"
GOOGLE_SHEETS = 'https://docs.google.com/spreadsheets/d/1eJ6FXLDYms009w4K0FDgVgDVF6cXzditrKtyMlh2j_k/edit#gid=0'


def get_abs_path(rel_path: str) -> str:
    return os.path.join(os.path.dirname(__file__), rel_path)
