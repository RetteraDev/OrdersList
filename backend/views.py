"""Доступные маршруты API"""
__author__ = 'RetteraDev'

from flask import jsonify, request

from app import app
from external_api.central_bank import get_USD_cost
from models.orders import get_orders, get_stats, get_orders_total


@app.route('/get_data')
def get_data_route():
    """Маршрут для получения заказов"""
    page = int(request.args.get('Page') or 0)
    limit = int(request.args.get('Limit') or 10)

    USD_cost = get_USD_cost()

    orders = []
    for order in get_orders(page, limit):
        orders.append({
            'Id': order.id,
            'OrderId': order.order_id,
            'CostUSD': order.cost,
            'CostRUB': order.cost * USD_cost,
            'DeliveryDate': order.delivery_date,
        })

    return jsonify({
        'HasMore': len(orders) == limit,
        'Orders': orders
    })


@app.route('/get_stats')
def get_stats_route():
    """Маршрут для получения статистики заказов"""
    USD_cost = get_USD_cost()

    total_orders, total_usd_cost = get_orders_total()
    total_rub_cost = total_usd_cost * USD_cost

    stats = []
    for stat in get_stats():
        stats.append({
            'DeliveryDate': stat[0],
            'CostUSD': stat[1],
            'CostRUB': stat[1] * USD_cost,
        })

    return jsonify({
        'Stats': stats,
        'TotalOrders': total_orders,
        'TotalCostUSD': total_usd_cost,
        'TotalCostRUB': total_rub_cost
    })