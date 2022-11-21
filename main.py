import os
from fastapi.exceptions import HTTPException
import uvicorn
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware, db

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from controllers.index import shop as route_ahop

import models
from db_conf import db_session

from services import shop, employee, customer, order, visit, crud_order, crud_visit
from models import Shop, OrderStatusEnum
from models import Shop as ModelShop
from schemas import ShopSchema
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
from models import Visit as ModelVisit
from schemas import BaseVisit as SchemaVisit

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

"""
Endpointы список торговых точек привязанных к номеру телефона
"""


@app.get("/shop_employee/{phone_number}", tags=["Список торговых точек привязанных к номеру телефона"])
def get_shops(phone_number: str):
    """
    Поиск торговой точки по номеру телефона 'Работника'. \n
    Из БД получается не список, а один объект 'Торговой точки',
    так как мне сказали, что по условиям один работник состоит только в одном магазине
    """
    employee = db.session.query(Employee).filter(Employee.phone_number == phone_number).first()
    if not employee:
        raise HTTPException(status_code=404, detail=f"Работника с таким номером телефона не существует!")
    return employee.shop


@app.get("/shop_customer/{phone_number}", tags=["Список торговых точек привязанных к номеру телефона"])
def get_shops(phone_number: str):
    """
    Поиск торговой точки по номеру телефона 'Заказчика'. \n
    Из БД получается не список, а один объект 'Торговой точки',
    так как мне сказали, что по условиям один работник состоит только в одном магазине
    """
    customer = db.session.query(Customer).filter(Customer.phone_number == phone_number).first()
    if not customer:
        raise HTTPException(status_code=404, detail=f"Заказчика с таким номером телефона не существует!")
    return customer.shop


"""
Endpointы CRUD по сущности 'Заказ'
"""


@app.get("/order/crud/{phone_number}", tags=["CRUD по сущности 'Заказ'"])
def get_orders(phone_number: str):
    """Получение всех заказов"""
    return crud_order.get_orders(phone_number=phone_number)


@app.post("/order/crud/{phone_number}", response_model=BaseOrderCustomer, tags=["CRUD по сущности 'Заказ'"])
def add_order(phone_number: str, order: BaseOrderCustomer):
    """Добавление заказа"""
    return crud_order.add_order(phone_number=phone_number, order=order)


@app.get("/order/crud/by_id/{phone_number}", tags=["CRUD по сущности 'Заказ'"])
def get_order_by_id(phone_number: str, order_id: int):
    return crud_order.get_order_by_id(phone_number=phone_number, order_id=order_id)


@app.put("/order/crud/{phone_number}", response_model=BaseOrderCustomer, tags=["CRUD по сущности 'Заказ'"])
def update_order(phone_number: str, order_id: int, order_data: BaseOrderCustomer):
    """
    Редактирование данных заказа. \n
    Применияются те же валидации, что и при создании 'Заказа'
    """
    return crud_order.update_order(phone_number=phone_number, order_id=order_id, order_data=order_data)


@app.delete("/order/crud/{phone_number}", tags=["CRUD по сущности 'Заказ'"])
def delete_order(phone_number: str, order_id: int):
    return crud_order.delete_order(phone_number=phone_number, order_id=order_id)


"""
Endpointы CRUD по сущности 'Посещение'
"""


@app.get("/visit/crud/{phone_number}", tags=["CRUD по сущности 'Посещение'"])
def get_visits(phone_number: str):
    """Получение всех посещении"""
    return crud_visit.get_visits(phone_number=phone_number)


@app.post("/visit/crud/{phone_number}", response_model=SchemaVisit, tags=["CRUD по сущности 'Посещение'"])
def add_visit(phone_number: str, visit: SchemaVisit):
    """Добавление посещения"""
    return crud_visit.add_visit(phone_number=phone_number, visit=visit)


@app.get("/visit/crud/by_id/{phone_number}", tags=["CRUD по сущности 'Посещение'"])
def get_visit_by_id(phone_number: str, visit_id: int):
    """Поиск посещения по id"""
    return crud_visit.get_visit_by_id(phone_number=phone_number, visit_id=visit_id)


@app.put("/visit/crud/{phone_number}", response_model=SchemaVisit, tags=["CRUD по сущности 'Посещение'"])
def update_visit(phone_number: str, visit_id: int, visit_data: SchemaVisit):
    """
    Редактирование данных посещения. \n
    Применияются те же валидации, что и при создании 'Посещения'
    """
    return crud_visit.update_visit(phone_number=phone_number, visit_id=visit_id, visit_data=visit_data)


@app.delete("/visit/crud/{phone_number}", tags=["CRUD по сущности 'Посещение'"])
def delete_visit(phone_number: str, visit_id: int):
    """Удаление посещения"""
    return crud_visit.delete_visit(phone_number=phone_number, visit_id=visit_id)


"""
Отдельный PUT метод для изменения статуса 'Заказа'
"""


@app.put("/order_status_change/{phone_number}",
         tags=["Отдельный PUT метод для изменения статуса 'Заказа'"], response_model=BaseOrderCustomer, )
def order_status_change(phone_number: str, order_id: int, status: OrderStatusEnum):
    """Отдельный PUT метод для изменения статуса 'Заказа'"""
    return crud_order.order_status_change(phone_number=phone_number, order_id=order_id, status=status)


"""
Endpointы для раздела админки 'Работник'
"""


@app.get("/employee/", tags=["Админка для сущности 'Работник'"])
def get_employees():
    """Получение списка работников"""
    return employee.get_employees()


@app.post("/employee/", response_model=SchemaEmployee, tags=["Админка для сущности 'Работник'"])
def add_employee(employee: SchemaEmployee):
    """Добавление работника"""
    employee_in_db = db.session.query(Employee).filter(employee.phone_number == Employee.phone_number).first()
    if employee_in_db:
        raise HTTPException(status_code=400, detail=f"Работник с таким номера телефона уже существует")
    db_employee = ModelEmployee(name=employee.name, phone_number=employee.phone_number, shop_id=employee.shop_id, )
    shop = db.session.query(Shop).filter(Shop.id == employee.shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует")
    db.session.add(db_employee)
    db.session.commit()
    return db_employee


@app.get("/employee/{employee_id}", tags=["Админка для сущности 'Работник'"])
def get_employee_by_id(employee_id: int):
    """Получение работника по id"""
    return employee.get_employee_by_id(employee_id=employee_id)


@app.get("/employee/name/{name_employee}", tags=["Админка для сущности 'Работник'"])
def get_employee_by_name(name_employee: str):
    """Поиск работника по имени"""
    return employee.get_employee_by_name_employee(name_employee=name_employee)


@app.get("/employee/phone_number/{phone_number}", tags=["Админка для сущности 'Работник'"])
def get_employee_by_numberr(phone_number: str):
    """Поиск работника по номеру телефона"""
    return employee.get_employee_by_number_employee(phone_number=phone_number)


@app.get("/employee/title_shop/{title_shop}", tags=["Админка для сущности 'Работник'"])
def get_employee_by_title_shop(title_shop: str):
    """Поиск работника по названию торговой точки"""
    return employee.get_employee_by_title_shop(title_shop=title_shop)


@app.put("/employee/{employee_id}", response_model=SchemaEmployee, tags=["Админка для сущности 'Работник'"])
def update_employee(employee_id: int, employee_data: SchemaEmployee):
    """Редактирование данных работника"""
    return employee.update_employee(employee_id=employee_id, employee_data=employee_data)


@app.delete("/employee/{employee_id}", tags=["Админка для сущности 'Работник'"])
def delete_employee(employee_id: int):
    """Удаление работника"""
    return employee.delete_employee(employee_id=employee_id)


"""
Endpointы для раздела админки 'Заказчик'
"""


@app.get("/customer/", tags=["Админка для сущности 'Заказчик'"])
def get_customers():
    """Получение всех заказчиков"""
    return customer.get_customers()


@app.post("/customer/", response_model=SchemaCustomer, tags=["Админка для сущности 'Заказчик'"])
def add_customer(customer: SchemaCustomer):
    """Создание заказчика"""
    validate_phone_number = db.session.query(Customer).filter(customer.phone_number == Customer.phone_number).first()
    if validate_phone_number:
        raise HTTPException(status_code=400, detail=f"Заказчик с таким номера телефона уже существует")
    db_customer = ModelCustomer(name=customer.name, phone_number=customer.phone_number, shop_id=customer.shop_id, )
    shop = db.session.query(Shop).filter(Shop.id == customer.shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail=f"Торговой точки не существует")
    db.session.add(db_customer)
    db.session.commit()
    return db_customer


@app.get("/customer/{customer_id}", tags=["Админка для сущности 'Заказчик'"])
def get_customer_by_id(customer_id: int):
    """Получение заказчика по id"""
    return customer.get_customer_by_id(customer_id=customer_id)


@app.get("/customer/name_employee/{name_employee}", tags=["Админка для сущности 'Заказчик'"])
def get_customer_by_name_employee(name_employee: str):
    """Поиск заказчика по имени работника"""
    return customer.get_customer_by_name_employee(name_employee=name_employee)


@app.get("/customer/phone_number_employee/{phone_number}", tags=["Админка для сущности 'Заказчик'"])
def get_customer_by_phone_number_employee(phone_number: str):
    """Поиск заказчика по номеру телефона работника"""
    return customer.get_customer_by_phone_number_employee(phone_number=phone_number)


@app.get("/customer/title_shop/{title_shop}", tags=["Админка для сущности 'Заказчик'"])
def get_customer_by_title_shop(title_shop: str):
    """Поиск заказчика по названию торговой точки"""
    return customer.get_customer_by_title_shop(title_shop=title_shop)


@app.put("/customer/{customer_id}", response_model=SchemaCustomer, tags=["Админка для сущности 'Заказчик'"])
def update_customer(customer_id: int, customer_data: SchemaCustomer):
    """Редактирование данных заказчика"""
    return customer.update_customer(customer_id=customer_id, customer_data=customer_data)


@app.delete("/customer/{customer_id}", tags=["Админка для сущности 'Заказчик'"])
def delete_customer(customer_id: int):
    """Удаление торговой точки"""
    return customer.delete_customer(customer_id=customer_id)


"""
Endpointы для раздела админки 'Торговая точка'
"""


@app.get("/shop/", tags=["Админка для сущности 'Торговая точка'"])
def get_shops():
    """Получение всех торговых точек"""
    return shop.get_list_shops()


@app.post("/shop/", response_model=ShopSchema, tags=["Админка для сущности 'Торговая точка'"])
def add_shop(shop: ShopSchema):
    """Добавление торговой точки"""
    db_shop = ModelShop(title=shop.title)
    db.session.add(db_shop)
    db.session.commit()
    return db_shop


@app.get("/shop/{shop_id}", tags=["Админка для сущности 'Торговая точка'"])
def get_shop_single_by_id(shop_id: int):
    """Получение торговой точки по id"""
    return shop.get_shop_single_by_id(shop_id=shop_id)


@app.get("/shop/name_employee/{name_employee}", tags=["Админка для сущности 'Торговая точка'"])
def get_shop_single_by_name_employee(name_employee: str):
    """Поиск торговой точки по имени работника"""
    return shop.get_shop_single_by_name_employee(name_employee=name_employee)


@app.get("/shop/phone_number_employee/{phone_number}", tags=["Админка для сущности 'Торговая точка'"])
def get_shop_single_by_phone_number_employee(phone_number: str):
    """Поиск торговой точки по номеру телефона работника"""
    return shop.get_shop_single_by_phone_number_employee(phone_number=phone_number)


@app.get("/shop/title_shop/{title_shop}", tags=["Админка для сущности 'Торговая точка'"])
def get_shop_single_by_title(title_shop: str):
    """Поиск по названию торговой точки"""
    return shop.get_shop_single_by_title(title_shop=title_shop)


@app.put("/shop/{shop_id}", response_model=ShopSchema, tags=["Админка для сущности 'Торговая точка'"])
def update_shop(shop_id: int, shop_data: ShopSchema):
    """Обновление торговой точки"""
    return shop.update_shop(shop_id=shop_id, shop_data=shop_data)


@app.delete("/shop/{shop_id}", tags=["Админка для сущности 'Торговая точка'"])
def delete_shop(shop_id: int):
    """Удаление торговой точки"""
    return shop.delete_shop(shop_id=shop_id)


"""
Endpointы для раздела админки 'Заказ'
"""


@app.get("/order/", tags=["Админка для сущности 'Заказ'"])
def get_orders():
    """Получение всех заказов"""
    return order.get_orders()


@app.post("/order/", response_model=BaseOrderCustomer, tags=["Админка для сущности 'Заказ'"])
def add_order(order: BaseOrderCustomer):
    """Добавление заказа"""
    validation_shop = db.session.query(Shop).filter(order.shop_id == Shop.id).all()
    if not validation_shop:
        raise HTTPException(status_code=400, detail=f"Торговой точки не существует")
    validation_author = db.session.query(Customer).filter(order.author_id == Customer.id).all()
    if not validation_author:
        raise HTTPException(status_code=400, detail=f"Такого заказчика не существует")
    validation_executor = db.session.query(Employee).filter(order.executor_id == Employee.id).all()
    if not validation_executor:
        raise HTTPException(status_code=400, detail=f"Такого работника не существует")
    db_order = ModelOrder(status=order.status, shop_id=order.shop_id,
                          author_id=order.author_id, executor_id=order.executor_id,
                          created_at=order.created_at, expiration_data=order.expiration_data)
    db.session.add(db_order)
    db.session.commit()
    return db_order


@app.get("/order/{order_id}", tags=["Админка для сущности 'Заказ'"])
def get_order_by_id(order_id: int):
    """Получение заказа по id"""
    return order.get_order_by_id(order_id=order_id)


@app.get("/order/name_employee/{name_employee}", tags=["Админка для сущности 'Заказ'"])
def get_order_by_name_employee(name_employee: str):
    """Поиск заказа по имени работника"""
    return order.get_order_by_name_employee(name_employee=name_employee)


@app.get("/order/phone_number_employee/{phone_number}", tags=["Админка для сущности 'Заказ'"])
def get_order_by_phone_number_employee(phone_number: str):
    """Поиск заказа по номеру телефона работника"""
    return order.get_order_by_phone_number_employee(phone_number=phone_number)


@app.get("/order/title_shop/{title_shop}", tags=["Админка для сущности 'Заказ'"])
def get_order_title_shop(title_shop: str):
    """Поиск заказа по названию торговой точки"""
    return order.get_order_title_shop(title_shop=title_shop)


@app.put("/order/{order_id}", response_model=BaseOrderCustomer, tags=["Админка для сущности 'Заказ'"])
def update_order(order_id: int, order_data: BaseOrderCustomer):
    """Редактирование данных заказа"""
    return order.update_order(order_id=order_id, order_data=order_data)


@app.delete("/order/{order_id}", tags=["Админка для сущности 'Заказ'"])
def delete_order(order_id: int):
    """Удаление заказа"""
    return order.delete_order(order_id=order_id)


"""
Endpointы для раздела админки 'Визит'
"""


@app.get("/visit/", tags=["Админка для сущности 'Посещение'"])
def get_visits():
    """Получение всех посещении"""
    return visit.get_visits()


@app.post("/visit/", response_model=SchemaVisit, tags=["Админка для сущности 'Посещение'"])
def add_visit(visit: SchemaVisit):
    """Добавление посещения"""

    validation_shop = db.session.query(Shop).filter(visit.shop_id == Shop.id).all()
    if not validation_shop:
        raise HTTPException(status_code=400, detail=f"Торговой точки не существует")

    validation_author = db.session.query(Customer).filter(visit.author_id == Customer.id).all()
    if not validation_author:
        raise HTTPException(status_code=400, detail=f"Такого заказчика не существует")

    validation_executor = db.session.query(Employee).filter(visit.executor_id == Employee.id).all()
    if not validation_executor:
        raise HTTPException(status_code=400, detail=f"Такого работника не существует")

    validation_order = db.session.query(Order).filter(visit.order_id == Order.id).all()
    if not validation_order:
        raise HTTPException(status_code=400, detail=f"Такого заказа не существует")

    db_visit = ModelVisit(shop_id=visit.shop_id,
                          author_id=visit.author_id,
                          executor_id=visit.executor_id,
                          order_id=visit.order_id,
                          created_at=visit.created_at)

    db.session.add(db_visit)
    db.session.commit()
    return db_visit


@app.get("/visit/{visit_id}", tags=["Админка для сущности 'Посещение'"])
def get_visit_by_id(visit_id: int):
    """Поиск посещения по id"""
    return visit.get_visit_by_id(visit_id=visit_id)


@app.get("/visit/name_employee/{name_employee}", tags=["Админка для сущности 'Посещение'"])
def get_visit_by_name_employee(name_employee: str):
    """Поиск посещения по имени работника"""
    return visit.get_visit_by_name_employee(name_employee=name_employee)


@app.get("/visit/phone_number_employee/{phone_number}", tags=["Админка для сущности 'Посещение'"])
def get_visit_by_phone_number_employee(phone_number: str):
    """Поиск посещения по номеру телефона работника"""
    return visit.get_visit_by_phone_number_employee(phone_number=phone_number)


@app.get("/visit/title_shop/{title_shop}", tags=["Админка для сущности 'Посещение'"])
def get_visit_title_shop(title_shop: str):
    """Поиск посещения по названию торговой точки"""
    return visit.get_visit_title_shop(title_shop=title_shop)


@app.put("/visit/{visit_id}", response_model=SchemaVisit, tags=["Админка для сущности 'Посещение'"])
def update_visit(visit_id: int, visit_data: SchemaVisit):
    """Редактирование данных посещения"""
    return visit.update_visit(visit_id=visit_id, visit_data=visit_data)


@app.delete("/visit/{visit_id}", tags=["Админка для сущности 'Посещение'"])
def delete_visit(visit_id: int):
    """Удаление заказа"""
    return visit.delete_visit(visit_id=visit_id)


app.include_router(route_ahop)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
