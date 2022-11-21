import os
from fastapi.exceptions import HTTPException
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Shop
from models import Employee
from models import Employee as ModelEmployee
from schemas import Employee as SchemaEmployee
from services.functions import get_employee_by_number, get_employee_by_name, get_shop_by_title
from models import Customer
from models import Customer as ModelCustomer
from schemas import Customer as SchemaCustomer

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


def get_customers():
    """Получение всех заказчиков"""
    customers = db.session.query(Customer).all()
    return customers


def add_customer(customer: SchemaCustomer):
    """Создание заказчика"""
    pass


def get_customer_by_id(customer_id: int):
    """Получение заказчика по id"""
    customer = db.session.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail=f"Заказчик не найден")
    return customer


def get_customer_by_name_employee(name_employee: str):
    """Поиск заказчика по имени работника"""
    employee = get_employee_by_name(name_employee=name_employee)
    shop = db.session.query(Shop).filter(Shop.id == employee.shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует")
    customer = db.session.query(Customer).filter(shop.id == Customer.shop_id).first()
    return customer


def get_customer_by_phone_number_employee(phone_number: str):
    """Поиск заказчика по номеру телефона работника"""
    employee = get_employee_by_number(phone_number=phone_number)
    shop = db.session.query(Shop).filter(Shop.id == employee.shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует")
    customer = db.session.query(Customer).filter(shop.id == Customer.shop_id).first()
    return customer


def get_customer_by_title_shop(title_shop: str):
    """Поиск заказчика по названию торговой точки"""
    shop = db.session.query(Shop).filter(Shop.title == title_shop).first()
    if not shop:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует")
    customer = db.session.query(Customer).filter(shop.id == Customer.shop_id).first()
    return customer


def update_customer(customer_id: int, customer_data: SchemaCustomer):
    """Редактирование данных заказчика"""
    customer = db.session.query(Customer).filter(Customer.id == customer_id).first()

    validate_phone_number = db.session.query(Customer).filter(
        customer_data.phone_number == Customer.phone_number).first()
    if validate_phone_number:
        raise HTTPException(status_code=400, detail=f"Заказчик с таким номера телефона уже существует")
    validate_shop = db.session.query(Shop).filter(customer_data.shop_id == Shop.id).first()
    if not validate_shop:
        raise HTTPException(status_code=400, detail=f"Торговой точки не существует")

    if customer:
        customer.name = customer_data.name
        customer.phone_number = customer_data.phone_number
        customer.shop_id = customer_data.shop_id
        db.session.commit()
    if not customer:
        raise HTTPException(status_code=404, detail=f"Заказчик не найден")
    return customer


def delete_customer(customer_id: int):
    """Удаление заказчика"""
    customer = db.session.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        db.session.delete(customer)
        db.session.commit()
        db.session.close()
    else:
        raise HTTPException(status_code=404, detail=f"Заказчик не найден")
    return None
