"""Получение данных от GoogleAPI SpreadSheets"""
__author__ = 'RetteraDev'

import gspread
from typing import Optional

from config import GOOGLE_SHEETS_SERVICE_ACCOUNT_KEY, GOOGLE_SHEETS, get_abs_path


gc = gspread.service_account(filename=get_abs_path(GOOGLE_SHEETS_SERVICE_ACCOUNT_KEY))
sheet = gc.open_by_url(GOOGLE_SHEETS).sheet1


def fetch_spreadsheet() -> Optional[list]:
    """Метод выполняет запрос на получение всех значений из таблицы
    Returns:
        data: list - Список значений
    """
    orders = sheet.get_all_values()
    return orders[1:] if orders else None
