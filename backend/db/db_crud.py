"""Операции над базой данных"""
__author__ = 'RetteraDev'

import psycopg2
from db.common import get_absolute_path
from external_api.google_sheets import fetch_spreadsheet


connection = psycopg2.connect(dbname='postgres', user='postgres', host="127.0.0.1", password='1', port=5432)
cursor = connection.cursor()


def get_all_records() -> list:
    """Метод получает все записи из базы в таблице orders
    Returns:
        records: list - Список записей
    """
    cursor.execute(open(get_absolute_path('sql/get_all_records.sql'), "r").read())
    return cursor.fetchall()


def update_records(new_records):
    """Метод выполняет обновление записей в базе
    Args:
        new_records - Список новых записей
    """
    if not new_records:
        return

    cursor.execute(open(get_absolute_path('sql/clear_records.sql'), "r").read())
    values = []
    for record in new_records:
        record_id = int(record[0])
        order_number = int(record[1])
        cost = int(record[2])
        delivery_date = record[3]
        values.append(str((record_id, order_number, cost, delivery_date)))

    update_request = f'INSERT INTO orders VALUES {", ".join(values)}'

    cursor.execute(update_request)
    connection.commit()


def init_db():
    """Метод выполняет первую инициализацию базы данных. Создает таблицу, если её еще нет и заполняет новыми значениями"""
    cursor.execute(open(get_absolute_path('sql/create_table.sql'), "r").read())
    connection.commit()

    update_records(fetch_spreadsheet())
