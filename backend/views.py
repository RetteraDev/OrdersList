"""Доступные маршруты API"""
__author__ = 'RetteraDev'

from flask import jsonify, request

from app import app
from external_api.central_bank import get_dollar_course
from models.orders import get_orders, get_stats


@app.route('/get_data')
def get_data_route():
    """Маршрут для получения заказов"""
    page = int(request.args.get('Page') or 0)
    limit = int(request.args.get('Limit') or 10)

    # Получим курс доллара от ЦБ РФ
    cost_of_dollar = get_dollar_course()

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


@app.route('/get_stats')
def get_stats_route():
    """Маршрут для получения статистики заказов"""
    stats = []
    for stat in get_stats():
        stats.append({
            'DeliveryDate': stat[0],
            'Costs': stat[1],
        })

    return jsonify({
        'Stats': stats
    })