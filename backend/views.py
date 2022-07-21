"""Доступные маршруты API"""
__author__ = 'RetteraDev'

from flask import jsonify, request
from app import app

from models.orders import get_orders


@app.route('/get_data')
def get_data():
    """Маршрут для получения заказов"""
    page = int(request.args.get('Page') or 0)
    limit = int(request.args.get('Limit') or 10)

    # Получим курс доллара с ЦБ РФ
    cost_of_dollar = 60

    orders = []
    for order in get_orders(page, limit):
        orders.append({
            'Id': order.id,
            'OrderId': order.order_id,
            'CostInDollars': order.cost,
            'CostInRubles': order.cost * cost_of_dollar,
            'DeliveryDate': order.delivery_date,
        })

    return jsonify({
        'HasMore': len(orders) == limit,
        'Orders': orders
    })
