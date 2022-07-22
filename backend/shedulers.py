"""Планировщики заданий по графику"""
__author__ = 'RetteraDev'

from flask_apscheduler import APScheduler
from models.orders import refill
from external_api.google_sheets import fetch_spreadsheet
from app import app

scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()

@scheduler.task('interval', id='fetch_spreadsheet')
def fetch_spreadsheet_job():
    refill(fetch_spreadsheet())
