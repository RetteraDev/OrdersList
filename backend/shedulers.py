"""Планировщики заданий по графику"""
__author__ = 'RetteraDev'

from apscheduler.schedulers.background import BackgroundScheduler
from models.orders import refill
from external_api.google_sheets import fetch_spreadsheet


scheduler = BackgroundScheduler(daemon=True)

# Обновление записей из Google Sheets каждые 10 секунд
scheduler.add_job(refill, 'interval', args=[fetch_spreadsheet()], seconds=10)

scheduler.start()
