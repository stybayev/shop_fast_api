import os
from fastapi.exceptions import HTTPException
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Shop, Customer
from models import Employee
from models import Employee as ModelEmployee
from schemas import Employee as SchemaEmployee
from services.functions import get_employee_by_number, get_employee_by_name, get_shop_by_title
from models import Order
from models import Order as ModelOrder
from schemas import BaseOrder as BaseOrderCustomer

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


def get_orders():
    """Получение всех заказов"""
    orders = db.session.query(Order).all()
    return orders


def add_order(order: BaseOrderCustomer):
    """Добавление заказа"""
    pass


def get_order_by_id(order_id: int):
    """Получение заказа по id"""
    order = db.session.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail=f"Заказ не найден")
    if order.visit:
        print(order.visit)
    return order


def get_order_by_name_employee(name_employee: str):
    """Поиск заказа по имени работника"""
    employee = get_employee_by_name(name_employee=name_employee)
    order = db.session.query(Order).filter(Order.executor_id == employee.id).all()
    if not order:
        raise HTTPException(status_code=404, detail=f"Заказы не найдены")
    return order


def get_order_by_phone_number_employee(phone_number: str):
    """Поиск заказа по номеру телефона работника"""
    employee = get_employee_by_number(phone_number=phone_number)
    order = db.session.query(Order).filter(Order.executor_id == employee.id).all()
    if not order:
        raise HTTPException(status_code=404, detail=f"Заказы не найдены")
    return order


def get_order_title_shop(title_shop: str):
    """Поиск заказа по названию торговой точки"""
    shop = get_shop_by_title(title_shop=title_shop)
    order = db.session.query(Order).filter(Order.shop_id == shop.id).all()
    if not order:
        raise HTTPException(status_code=404, detail=f"Заказы не найдены")
    return order


def update_order(order_id: int, order_data: BaseOrderCustomer):
    """Редактирование данных заказа"""
    order = db.session.query(Order).filter(Order.id == order_id).first()

    validate_shop_id = db.session.query(Shop).filter(
        order_data.shop_id == Shop.id).first()
    if not validate_shop_id:
        raise HTTPException(status_code=404, detail=f"Торговой точки существует")

    validate_author_id = db.session.query(Customer).filter(
        order_data.author_id == Customer.id).first()
    if not validate_author_id:
        raise HTTPException(status_code=404, detail=f"Такого заказчика не нашли")

    validate_executor_id = db.session.query(Employee).filter(
        order_data.executor_id == Employee.id).first()
    if not validate_executor_id:
        raise HTTPException(status_code=404, detail=f"Такого работника не нашли")

    if order:
        order.status = order_data.status
        order.shop_id = order_data.shop_id
        order.author_id = order_data.author_id
        order.executor_id = order_data.executor_id
        order.created_at = order_data.created_at
        order.expiration_data = order_data.expiration_data
        db.session.commit()

    if not order:
        raise HTTPException(status_code=404, detail=f"Заказ не найден")
    return order


def delete_order(order_id: int):
    """Удаление заказа"""
    order = db.session.query(Order).filter(Order.id == order_id).first()
    if order:
        db.session.delete(order)
        db.session.commit()
        db.session.close()
    else:
        raise HTTPException(status_code=404, detail=f"Заказ не найден")
    return None
