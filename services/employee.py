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

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


def get_employees():
    """Получение списка работников"""
    employees = db.session.query(Employee).all()
    return employees


def add_employee(employee: SchemaEmployee):
    """Добавление работника"""
    pass


def get_employee_by_id(employee_id: int):
    """Получение работника по id"""
    employee = db.session.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail=f"Работник не найден")
    return employee


def get_employee_by_name_employee(name_employee: str):
    """Поиск работника по имени"""
    employee = db.session.query(Employee).filter(Employee.name == name_employee).all()
    if not employee:
        raise HTTPException(status_code=404, detail=f"Работника с таким именем не существует")
    return employee


def get_employee_by_number_employee(phone_number: str):
    """Поиск работника по номеру телефона"""
    return get_employee_by_number(phone_number=phone_number)


def get_employee_by_title_shop(title_shop: str):
    """Поиск работника по названию торговой точки"""
    shop = get_shop_by_title(title_shop=title_shop)
    employee = db.session.query(Employee).filter(shop.id == Employee.shop_id).all()
    if not employee:
        raise HTTPException(status_code=404, detail=f"Работник не найден")
    return employee


def update_employee(employee_id: int, employee_data: SchemaEmployee):
    """Редактирование данных работника"""
    employee = db.session.query(Employee).filter(Employee.id == employee_id).first()

    validate_phone_number = db.session.query(Employee).filter(employee_data.phone_number == Employee.phone_number).first()
    if validate_phone_number:
        raise HTTPException(status_code=400, detail=f"Работник с таким номера телефона уже существует")
    validate_shop = db.session.query(Shop).filter(employee_data.shop_id == Shop.id).first()
    if not validate_shop:
        raise HTTPException(status_code=400, detail=f"Торговой точки не существует")

    if employee:
        employee.name = employee_data.name
        employee.phone_number = employee_data.phone_number
        employee.shop_id = employee_data.shop_id
        db.session.commit()
    if not employee:
        raise HTTPException(status_code=404, detail=f"Работник не найден")
    return employee


def delete_employee(employee_id: int):
    """Удаление работника"""
    employee = db.session.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        db.session.delete(employee)
        db.session.commit()
        db.session.close()
    else:
        raise HTTPException(status_code=404, detail=f"Работник не найден")
    return None
