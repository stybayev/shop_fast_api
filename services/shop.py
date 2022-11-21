import os
from fastapi.exceptions import HTTPException
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Shop
from models import Shop as ModelShop
from schemas import ShopSchema
from services.functions import get_employee_by_number, get_employee_by_name

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


def get_list_shops():
    shops = db.session.query(Shop).all()
    return shops


def add_shop(shop: ShopSchema):
    """Добавление торговой точки"""
    db_shop = ModelShop(title=shop.title)
    db.session.add(db_shop)
    db.session.commit()
    return db_shop


def get_shops(phone_number: str):
    employee = get_employee_by_number(phone_number=phone_number)
    shops = db.session.query(Shop).all()
    return {'employee': employee,
            'shops': shops}


def get_shop_single_by_id(shop_id: int):
    """Получение торговой точки по id"""
    shop = db.session.query(Shop).filter(Shop.id == shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует")
    return shop


def get_shop_single_by_name_employee(name_employee: str):
    """Поиск торговой точки по имени работника"""
    employee = get_employee_by_name(name_employee=name_employee)
    shop = db.session.query(Shop).filter(Shop.id == employee.shop_id).all()
    if not shop:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует")
    return shop


def get_shop_single_by_phone_number_employee(phone_number: str):
    """Поиск торговой точки по номеру телефона работника"""
    employee = get_employee_by_number(phone_number=phone_number)
    shop = db.session.query(Shop).filter(Shop.id == employee.shop_id).all()
    if not shop:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует")
    return shop


def get_shop_single_by_title(title_shop: str):
    """Поиск по названию торговой точки"""
    shop = db.session.query(Shop).filter(Shop.title == title_shop).all()
    if not shop:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует")
    return shop


def update_shop(shop_id: int, shop_data: ShopSchema):
    """Обновление торговой точки"""
    shop = db.session.query(Shop).filter(Shop.id == shop_id).first()
    if shop:
        shop.title = shop_data.title
        db.session.commit()
    if not shop:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует")
    return shop


def delete_shop(shop_id: int):
    """Удаление торговой точки"""
    shop = db.session.query(Shop).filter(Shop.id == shop_id).first()
    if shop:
        db.session.delete(shop)
        db.session.commit()
        db.session.close()
    else:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует")
    return None
