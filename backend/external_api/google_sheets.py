"""Получение данных от GoogleAPI SpreadSheets"""
__author__ = 'RetteraDev'

import gspread
from typing import Optional


gc = gspread.service_account()
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1eJ6FXLDYms009w4K0FDgVgDVF6cXzditrKtyMlh2j_k/edit#gid=0').sheet1


def fetch_spreadsheet() -> Optional[list]:
    """Метод выполняет запрос на получение всех значений из таблицы
    Returns:
        data: list - Список значений
    """
    orders = sheet.get_all_values()
    return orders[1:] if orders else None
