import os
from fastapi.exceptions import HTTPException
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from services import shop, employee, customer, order
from models import Shop
from models import Shop as ModelShop
from schemas import Shop as SchemaShop

from models import Employee
from models import Employee as ModelEmployee
from schemas import Employee as SchemaEmployee

from models import Customer
from models import Customer as ModelCustomer
from schemas import Customer as SchemaCustomer

from models import Order
from models import Order as ModelOrder
from schemas import BaseOrder as BaseOrderCustomer

from models import Visit
from models import Order as ModelVisit
from schemas import BaseVisit as SchemaVisit
from services.functions import get_employee_by_name, get_employee_by_number, get_shop_by_title

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


def get_visits():
    """Получение всех посещении"""
    visits = db.session.query(Visit).all()
    return visits


def add_visit(visit: SchemaVisit):
    """Добавление посещения"""
    pass


def get_visit_by_id(visit_id: int):
    """Поиск посещения по id"""
    visit = db.session.query(Visit).filter(Visit.id == visit_id).first()
    if not visit:
        raise HTTPException(status_code=404, detail=f"Посещение не найдено")
    return visit


def get_visit_by_name_employee(name_employee: str):
    """Поиск посещения по имени работника"""
    employee = get_employee_by_name(name_employee=name_employee)
    print(employee.id, employee.name)
    visit = db.session.query(Visit).filter(Visit.executor_id == employee.id).all()
    if not visit:
        raise HTTPException(status_code=404, detail=f"Посещения не найдены")
    return visit


def get_visit_by_phone_number_employee(phone_number: str):
    """Поиск посещения по номеру телефона работника"""
    employee = get_employee_by_number(phone_number=phone_number)
    visit = db.session.query(Visit).filter(Visit.executor_id == employee.id).all()
    if not visit:
        raise HTTPException(status_code=404, detail=f"Посещения не найдены")
    return visit


def get_visit_title_shop(title_shop: str):
    """Поиск посещения по названию торговой точки"""
    shop = get_shop_by_title(title_shop=title_shop)
    visit = db.session.query(Visit).filter(Visit.shop_id == shop.id).all()
    if not visit:
        raise HTTPException(status_code=404, detail=f"Посещения не найдены")
    return visit


def update_visit(visit_id: int, visit_data: SchemaVisit):
    """Редактирование данных посещения"""
    visit = db.session.query(Visit).filter(Visit.id == visit_id).first()

    validate_shop_id = db.session.query(Shop).filter(
        visit_data.shop_id == Shop.id).first()
    if not validate_shop_id:
        raise HTTPException(status_code=404, detail=f"Торговой точки существует")

    validate_author_id = db.session.query(Customer).filter(
        visit_data.author_id == Customer.id).first()
    if not validate_author_id:
        raise HTTPException(status_code=404, detail=f"Такого заказчика не нашли")

    validate_executor_id = db.session.query(Employee).filter(
        visit_data.executor_id == Employee.id).first()
    if not validate_executor_id:
        raise HTTPException(status_code=404, detail=f"Такого работника не нашли")

    if visit:
        visit.shop_id = visit_data.shop_id
        visit.author_id = visit_data.author_id
        visit.executor_id = visit_data.executor_id
        visit.created_at = visit_data.created_at
        db.session.commit()

    if not visit:
        raise HTTPException(status_code=404, detail=f"Посещение не найдено")
    return visit


@app.delete("/visit/{visit_id}", tags=["Админка для раздела 'Визит'"])
def delete_visit(visit_id: int):
    """Удаление посещения"""
    visit = db.session.query(Visit).filter(Visit.id == visit_id).first()
    if visit:
        db.session.delete(visit)
        db.session.commit()
        db.session.close()
    else:
        raise HTTPException(status_code=404, detail=f"Посещение не найдено")
    return None
