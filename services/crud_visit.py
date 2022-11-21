import os
from fastapi.exceptions import HTTPException
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Shop

from models import Employee

from models import Customer

from models import Order

from models import Visit
from models import Visit as ModelVisit
from schemas import BaseVisit as SchemaVisit

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


def get_visits(phone_number: str):
    """Получение всех посещении"""
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if customer:
        orders = db.session.query(Visit).all()
        return orders
    else:
        raise HTTPException(status_code=400, detail=f"Таких работников не нашли")


def add_visit(phone_number: str, visit: SchemaVisit):
    """Добавление посещения"""
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if not customer:
        raise HTTPException(status_code=400, detail=f"Такого заказчика не существует")

    shop = db.session.query(Shop).filter(visit.shop_id == customer.shop_id).first()
    if not shop:
        raise HTTPException(status_code=400,
                            detail=f"Заказчик может создать 'Посещение' только на свою 'Торговую точку'")

    author = db.session.query(Customer).filter(visit.author_id == customer.id).first()
    if not author:
        raise HTTPException(status_code=400, detail=f"Автором может быть только текущий заказачик")

    order = db.session.query(Order).filter(visit.order_id == Order.id).first()
    if not order:
        raise HTTPException(status_code=400, detail=f"Заказ не найден")
    if order.expiration_data.timestamp() < visit.created_at.timestamp():
        raise HTTPException(status_code=400, detail=f"Срок 'Заказа' истек")

    if order.visit:
        raise HTTPException(status_code=400,
                            detail=f"Посещение может создаваться, если ранее уже не было иной записи по PK 'Заказа'")

    executor = db.session.query(Employee).filter(visit.executor_id == order.executor_id).first()
    if not executor:
        raise HTTPException(status_code=400,
                            detail=f"Исполнителем должен быть Работник привязанным к 'Заказу'")

    db_visit = ModelVisit(shop_id=visit.shop_id,
                          author_id=visit.author_id,
                          executor_id=visit.executor_id,
                          order_id=visit.order_id,
                          created_at=visit.created_at)

    db.session.add(db_visit)
    db.session.commit()
    return db_visit


def get_visit_by_id(phone_number: str, visit_id: int):
    """Поиск посещения по id"""
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if customer:
        visit = db.session.query(Visit).filter(Visit.id == visit_id).first()
        if not visit:
            raise HTTPException(status_code=404, detail=f"Посещение не найдено")
        if visit.order:
            print(visit.order)
        return visit
    else:
        raise HTTPException(status_code=400, detail=f"Таких работников не нашли")


def update_visit(phone_number: str, visit_id: int, visit_data: SchemaVisit):
    """Редактирование данных посещения"""
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if not customer:
        raise HTTPException(status_code=400, detail=f"Такого заказчика не существует")

    shop = db.session.query(Shop).filter(visit_data.shop_id == customer.shop_id).first()
    if not shop:
        raise HTTPException(status_code=400, detail=f"Заказчик может обновить заказ только на свою Торговую точку")

    author = db.session.query(Customer).filter(visit_data.author_id == customer.id).first()
    if not author:
        raise HTTPException(status_code=400, detail=f"Автором может быть только текущий заказачик")

    order = db.session.query(Order).filter(visit_data.order_id == Order.id).first()
    if not order:
        raise HTTPException(status_code=400, detail=f"Заказ не найден")
    if order.expiration_data.timestamp() < visit_data.created_at.timestamp():
        raise HTTPException(status_code=400, detail=f"Срок 'Заказа' истек")

    executor = db.session.query(Employee).filter(visit_data.executor_id == order.executor_id).first()
    if not executor:
        raise HTTPException(status_code=400,
                            detail=f"Исполнителем должен быть Работник привязанным к 'Заказу'")

    visit_db = db.session.query(Visit).filter(Visit.id == visit_id).first()

    if visit_db:
        visit_db.shop_id = visit_data.shop_id
        visit_db.author_id = visit_data.author_id
        visit_db.executor_id = visit_data.executor_id
        visit_db.created_at = visit_data.created_at
        visit_db.order_id = visit_data.order_id
        db.session.commit()

    if not visit_db:
        raise HTTPException(status_code=404, detail=f"Посещение не найдено")
    return visit_db


def delete_visit(phone_number: str, visit_id: int):
    """Удаление посещения"""
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if not customer:
        raise HTTPException(status_code=400, detail=f"Такого заказчика не существует")
    visit = db.session.query(Visit).filter(visit_id == Visit.id).first()
    if visit and visit.author_id == customer.id:
        db.session.delete(visit)
        db.session.commit()
        db.session.close()
    else:
        raise HTTPException(status_code=404, detail=f"Заказчик может удалить только свой посещения")
    return None
