"""Планировщики заданий по графику"""
__author__ = 'RetteraDev'

from apscheduler.schedulers.background import BackgroundScheduler
from db.db_crud import update_records
from external_api.google_sheets import fetch_spreadsheet


scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(update_records, 'interval', args=[fetch_spreadsheet()], minutes=5)
scheduler.start()
