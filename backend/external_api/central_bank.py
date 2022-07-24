"""Получение данных от ЦБ РФ"""
__author__ = 'RetteraDev'

from pycbrf.toolbox import ExchangeRates
from datetime import date


def get_USD_cost() -> float:
    return ExchangeRates(date.today())['USD'].value
