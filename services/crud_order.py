import os
from fastapi.exceptions import HTTPException
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Shop, OrderStatusEnum

from models import Employee

from models import Customer

from models import Order
from models import Order as ModelOrder
from schemas import BaseOrder as BaseOrderCustomer

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


def get_orders(phone_number: str):
    """Получение всех заказов"""
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if customer:
        orders = db.session.query(Order).all()
        return orders
    else:
        raise HTTPException(status_code=400, detail=f"Таких работников не нашли")


def add_order(phone_number: str, order: BaseOrderCustomer):
    """Добавление заказа"""
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if not customer:
        raise HTTPException(status_code=400, detail=f"Такого заказчика не существует")

    shop = db.session.query(Shop).filter(order.shop_id == customer.shop_id).first()
    if not shop:
        raise HTTPException(status_code=400, detail=f"Заказчик может создать заказ только на свою Торговую точку")

    author = db.session.query(Customer).filter(order.author_id == customer.id).first()
    if not author:
        raise HTTPException(status_code=400, detail=f"Автором может быть только текущий заказачик")

    executor = db.session.query(Employee).filter(order.executor_id == Employee.id).first()
    if not executor:
        raise HTTPException(status_code=400, detail=f"Такого исполнителя не существует")
    if executor.shop_id != order.shop_id:
        raise HTTPException(status_code=400, detail=f"Исполнителем должен быть работник привязанным к торговой точке")
    db_order = ModelOrder(status=order.status, shop_id=order.shop_id,
                          author_id=order.author_id, executor_id=order.executor_id,
                          created_at=order.created_at, expiration_data=order.expiration_data)

    db.session.add(db_order)
    db.session.commit()
    return db_order


def get_order_by_id(phone_number: str, order_id: int):
    """Получение заказа по id"""
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if customer:
        order = db.session.query(Order).filter(Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=404, detail=f"Заказ не найден")
        if order.visit:
            print(order.visit)
        return order
    else:
        raise HTTPException(status_code=400, detail=f"Таких работников не нашли")


def update_order(phone_number: str, order_id: int, order_data: BaseOrderCustomer):
    """Редактирование данных заказа"""
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if not customer:
        raise HTTPException(status_code=400, detail=f"Такого заказчика не существует")

    order = db.session.query(Order).filter(Order.id == order_id).first()

    shop = db.session.query(Shop).filter(order_data.shop_id == customer.shop_id).first()
    if not shop:
        raise HTTPException(status_code=400, detail=f"Заказчик может обновить заказ только на свою Торговую точку")

    author = db.session.query(Customer).filter(order_data.author_id == customer.id).first()
    if not author:
        raise HTTPException(status_code=400, detail=f"Автором может быть только текущий заказачик")

    executor = db.session.query(Employee).filter(order_data.executor_id == Employee.id).first()
    if not executor:
        raise HTTPException(status_code=400, detail=f"Такого исполнителя не существует")
    if executor.shop_id != order_data.shop_id:
        raise HTTPException(status_code=400, detail=f"Исполнителем должен быть работник привязанным к торговой точке")

    if order and order.author_id == customer.id:
        order.status = order_data.status
        order.shop_id = order_data.shop_id
        order.author_id = order_data.author_id
        order.executor_id = order_data.executor_id
        order.created_at = order_data.created_at
        order.expiration_data = order_data.expiration_data
        db.session.commit()
    else:
        raise HTTPException(status_code=400, detail=f"Заказчик может обновить только свой заказы")
    return order


def delete_order(phone_number: str, order_id: int):
    """Удаление заказа"""
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if not customer:
        raise HTTPException(status_code=400, detail=f"Такого заказчика не существует")
    order = db.session.query(Order).filter(order_id == Order.id).first()
    if order and order.author_id == customer.id:
        db.session.delete(order)
        db.session.commit()
        db.session.close()
    else:
        raise HTTPException(status_code=404, detail=f"Заказчик может удалить только свой заказы")
    return None


def order_status_change(phone_number: str, order_id: int, status: OrderStatusEnum):
    """Отдельный PUT метод для изменения статуса 'Заказа'"""
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if not customer:
        raise HTTPException(status_code=400, detail=f"Такого заказчика не существует")
    order = db.session.query(Order).filter(Order.id == order_id).first()
    if order and order.author_id == customer.id:
        order.status = status
        db.session.commit()
    else:
        raise HTTPException(status_code=400, detail=f"Заказчик может обновить только свои заказы")
    return order
