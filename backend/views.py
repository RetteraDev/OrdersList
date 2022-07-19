"""Доступные маршруты API"""
__author__ = 'RetteraDev'

from flask import jsonify
from app import app

from db.db_crud import get_all_records


@app.route('/get_data')
def hello():
    return jsonify({'orders': get_all_records()})
