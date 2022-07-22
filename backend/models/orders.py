"""Модель таблицы заказов и операции над ней"""
__author__ = 'RetteraDev'

from sqlalchemy.sql import func
from datetime import date

from app import db


class Order(db.Model):
    """Таблица с заказами"""
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    delivery_date = db.Column(db.DateTime)

    def __init__(self, id: int, order_id: int, cost: int, delivery_date: date) -> None:
        """Создание объекта заказа
        Args:
            id - Идентификатор записи
            order_id - Идентификатор заказа
            cost - Стоимость в долларах
            delivery_date - Дата поставки
        """
        self.id = id
        self.order_id = order_id
        self.cost = cost
        self.delivery_date = delivery_date


def refill(orders: list) -> None:
    """Метод выполняет перезапись в базу данных новыми настройками из таблицы
    Args:
        orders - Список записей заказов
    """
    # Если записей нет, ничего не делаем
    if not orders:
        return
    # Удалим старые записи
    Order.query.delete()
    db.session.commit()

    # Запишем новые
    db.session.add_all([Order(*order) for order in orders])
    db.session.commit()


def get_orders(page: int, limit: int) -> list:
    """Метод возвращает значения для списка заказов с пагинацией
    Args:
        page - Страница запроса
        limit - Лимит записей
    """
    return db.session.query(Order).limit(limit).offset(page * limit).all()


def get_stats() -> list:
    """Метод возвращает значения для списка заказов с пагинацией
    Args:
        page - Страница запроса
        limit - Лимит записей
    """
    return db.session.query(Order.delivery_date, func.sum(Order.cost)).group_by(Order.delivery_date).all()
