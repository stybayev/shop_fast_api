import os
from fastapi.exceptions import HTTPException
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from models import Employee, Shop

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


def get_employee_by_name(name_employee: str):
    employee = db.session.query(Employee).filter(Employee.name == name_employee).first()
    if not employee:
        raise HTTPException(status_code=404, detail=f"Работника с таким именем не существует")
    return employee


def get_employee_by_number(phone_number: str):
    employee = db.session.query(Employee).filter(Employee.phone_number == phone_number).first()
    if not employee:
        raise HTTPException(status_code=404, detail=f"Работника с таки номером телефона не существует!")
    return employee


def get_shop_by_title(title_shop: str):
    shop = db.session.query(Shop).filter(Shop.title == title_shop).first()
    if not shop:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует!")
    return shop
