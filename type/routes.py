import enum
import typing
import os
from datetime import datetime

import strawberry
from fastapi_sqlalchemy import DBSessionMiddleware, db
from strawberry.types import Info
from dotenv import load_dotenv
from fastapi import FastAPI
from models import Shop as ModelShop
from fastapi.exceptions import HTTPException
from models import Employee as ModelEmployee
from models import Customer as ModelCustomer
from models import Order as ModelOrder
from models import Visit as ModelVisit

from fastapi import Body

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@strawberry.type
class Shop:
    id: int
    title: str


@strawberry.type
class Employee:
    name: str
    phone_number: str
    shop_id: int


@strawberry.type
class Customer:
    name: str
    phone_number: str
    shop_id: int


@strawberry.enum
class OrderStatusEnum(enum.Enum):
    started = 'started'
    ended = 'ended'
    in_process = 'in process'
    awaiting = 'awaiting'
    canceled = 'canceled'


@strawberry.type
class Order:
    status: str
    shop_id: int
    author_id: int
    executor_id: int
    created_at: typing.Union[datetime, None] = Body(default=datetime.now())
    expiration_data: typing.Union[datetime, None] = Body(default=datetime.now())


@strawberry.type
class Visit:
    shop_id: int
    author_id: int
    executor_id: int
    order_id: int
    created_at: typing.Union[datetime, None] = Body(default=datetime.now())


@strawberry.type
class Query:
    """Shop"""

    @strawberry.field
    async def get_shop_by_phone_number_employee(self, phone_number: str) -> Shop:
        """
        Поиск торговой точки по номеру телефона 'Работника'. \n
        Из БД получается не список, а один объект 'Торговой точки',
        так как мне сказали, что по условиям один работник состоит только в одном магазине
        """
        employee = db.session.query(ModelEmployee).filter(ModelEmployee.phone_number == phone_number).first()
        if not employee:
            raise ValueError(f"Работника с таким номером телефона не существует!")
        return employee.shop

    @strawberry.field
    async def get_shop_by_phone_number_customer(self, phone_number: str) -> Shop:
        """
        Поиск торговой точки по номеру телефона 'Заказчика'. \n
        Из БД получается не список, а один объект 'Торговой точки',
        так как мне сказали, что по условиям один работник состоит только в одном магазине
        """
        customer = db.session.query(ModelCustomer).filter(ModelCustomer.phone_number == phone_number).first()
        if not customer:
            raise ValueError(f"Заказчика с таким номером телефона не существует!")
        return customer.shop

    @strawberry.field
    async def shop(self, id: int) -> Shop:
        return db.session.query(ModelShop).filter(ModelShop.id == id).first()

    @strawberry.field
    async def list_shops(self) -> typing.List[Shop]:
        return db.session.query(ModelShop).all()

    """Employee"""

    @strawberry.field
    async def empolyee(self, id: int) -> Employee:
        return db.session.query(ModelEmployee).filter(ModelEmployee.id == id).first()

    @strawberry.field
    async def list_empolyees(self) -> typing.List[Employee]:
        return db.session.query(ModelEmployee).all()

    """Customer"""

    @strawberry.field
    async def customer(self, id: int) -> Customer:
        return db.session.query(ModelCustomer).filter(ModelCustomer.id == id).first()

    @strawberry.field
    async def list_customers(self) -> typing.List[Customer]:
        return db.session.query(ModelCustomer).all()

    """Order"""

    @strawberry.field
    async def order(self, id: int) -> Order:
        return db.session.query(ModelOrder).filter(ModelOrder.id == id).first()

    @strawberry.field
    async def list_orders(self) -> typing.List[Order]:
        return db.session.query(ModelOrder).all()

    """Visit"""

    @strawberry.field
    async def visit(self, id: int) -> Visit:
        return db.session.query(ModelVisit).filter(ModelVisit.id == id).first()

    @strawberry.field
    async def list_visits(self) -> typing.List[Visit]:
        return db.session.query(ModelVisit).all()


@strawberry.type
class Mutation:
    """Shop"""

    @strawberry.mutation
    async def create_shop(self, title: str, info: Info) -> int:
        db_shop = ModelShop(title=title)
        db.session.add(db_shop)
        db.session.commit()
        return db_shop.id

    @strawberry.mutation
    async def update_shop(self, id: int, title: str, info: Info) -> str:
        shop = db.session.query(ModelShop).filter(ModelShop.id == id).first()
        shop.title = title
        db.session.commit()
        return f"'Title' fields updated successfully"

    @strawberry.mutation
    async def delete_shop(self, id: int) -> str:
        shop = db.session.query(ModelShop).filter(ModelShop.id == id).first()
        db.session.delete(shop)
        db.session.commit()
        db.session.close()
        return f"Object deleted successfully"

    "Employee"

    @strawberry.mutation
    async def create_empolyee(self, name: str, phone_number: str, shop_id: int) -> int:
        db_empolyee = ModelEmployee(name=name, phone_number=phone_number, shop_id=shop_id)
        db.session.add(db_empolyee)
        db.session.commit()
        return db_empolyee.id

    @strawberry.mutation
    async def update_empolyee(self, id: int, name: str, phone_number: str, shop_id: int) -> str:
        employee = db.session.query(ModelEmployee).filter(ModelEmployee.id == id).first()
        employee.name = name
        employee.phone_number = phone_number
        employee.shop_id = shop_id
        db.session.commit()
        return f"Fields updated successfully"

    @strawberry.mutation
    async def delete_empolyee(self, id: int) -> str:
        employee = db.session.query(ModelEmployee).filter(ModelEmployee.id == id).first()
        db.session.delete(employee)
        db.session.commit()
        db.session.close()
        return f"Object deleted successfully"

    "Customer"

    @strawberry.mutation
    async def create_customer(self, name: str, phone_number: str, shop_id: int) -> int:
        db_customer = ModelCustomer(name=name, phone_number=phone_number, shop_id=shop_id)
        db.session.add(db_customer)
        db.session.commit()
        return db_customer.id

    @strawberry.mutation
    async def update_customer(self, id: int, name: str, phone_number: str, shop_id: int) -> str:
        customer = db.session.query(ModelCustomer).filter(ModelCustomer.id == id).first()
        customer.name = name
        customer.phone_number = phone_number
        customer.shop_id = shop_id
        db.session.commit()
        return f"Fields updated successfully"

    @strawberry.mutation
    async def delete_customer(self, id: int) -> str:
        customer = db.session.query(ModelCustomer).filter(ModelCustomer.id == id).first()
        db.session.delete(customer)
        db.session.commit()
        db.session.close()
        return f"Object deleted successfully"

    """Order"""

    @strawberry.mutation
    async def create_order(self, phone_number_customer: str, status: OrderStatusEnum, shop_id: int, author_id: int,
                           executor_id: int,
                           created_at: datetime = datetime.now(), expiration_data: datetime = datetime.now()) -> int:
        customer = db.session.query(ModelCustomer).filter(ModelCustomer.phone_number == phone_number_customer).first()
        if not customer:
            raise ValueError("Такого заказчика не существует")

        shop = db.session.query(ModelShop).filter(shop_id == customer.shop_id).first()
        if not shop:
            raise ValueError("Заказчик может создать заказ только на свою Торговую точку")

        author = db.session.query(ModelShop).filter(author_id == customer.id).first()
        if not author:
            raise ValueError("Автором может быть только текущий заказачик")

        executor = db.session.query(ModelEmployee).filter(executor_id == ModelEmployee.id).first()
        if not executor:
            raise ValueError(f"Такого исполнителя не существует")
        if executor.shop_id != shop_id:
            raise ValueError(f"Исполнителем должен быть работник привязанным к торговой точке")

        db_order = ModelOrder(status=str(status.name), shop_id=shop_id, author_id=author_id,
                              executor_id=executor_id, created_at=created_at, expiration_data=expiration_data)

        db.session.add(db_order)
        db.session.commit()
        return db_order.id

    @strawberry.mutation
    async def update_order(self, phone_number_customer: str, id: int, status: OrderStatusEnum,
                           created_at: datetime = datetime.now(),
                           expiration_data: datetime = datetime.now()) -> str:

        customer = db.session.query(ModelCustomer).filter(ModelCustomer.phone_number == phone_number_customer).first()
        if not customer:
            raise ValueError("Такого заказчика не существует")

        order = db.session.query(ModelOrder).filter(ModelOrder.id == id).first()
        if order and order.author_id == customer.id:
            order.status = str(status.name)
            order.created_at = created_at
            order.expiration_data = expiration_data
            db.session.commit()
        else:
            raise ValueError("Заказчик может обновить только свой заказы")
        return f"Fields updated successfully"

    @strawberry.mutation
    async def delete_order(self, phone_number_customer: str, order_id: int) -> str:
        customer = db.session.query(ModelCustomer).filter(ModelCustomer.phone_number == phone_number_customer).first()
        if not customer:
            raise ValueError("Такого заказчика не существует")

        order = db.session.query(ModelOrder).filter(order_id == ModelOrder.id).first()
        if order and order.author_id == customer.id:
            db.session.delete(order)
            db.session.commit()
            db.session.close()
        else:
            raise ValueError("Заказчик может удалить только свой заказы")
        return f"Object deleted successfully"

    """Visit"""

    @strawberry.mutation
    async def create_visit(self,
                           phone_number_customer: str,
                           shop_id: int,
                           author_id: int,
                           executor_id: int,
                           order_id: int,
                           created_at: datetime = datetime.now()) -> int:

        customer = db.session.query(ModelCustomer).filter(ModelCustomer.phone_number == phone_number_customer).first()
        if not customer:
            raise ValueError(f"Такого заказчика не существует")

        shop = db.session.query(ModelShop).filter(shop_id == customer.shop_id).first()
        if not shop:
            raise ValueError(f"Заказчик может создать 'Посещение' только на свою 'Торговую точку'")

        author = db.session.query(ModelCustomer).filter(author_id == customer.id).first()
        if not author:
            raise ValueError(f"Автором может быть только текущий заказачик")

        order = db.session.query(ModelOrder).filter(order_id == ModelOrder.id).first()
        if not order:
            raise ValueError(f"Заказ не найден")
        if order.expiration_data.timestamp() < created_at.timestamp():
            raise ValueError(f"Срок 'Заказа' истек")

        if order.visit:
            raise ValueError(f"Посещение может создаваться, если ранее уже не было иной записи по PK 'Заказа'")

        executor = db.session.query(ModelEmployee).filter(executor_id == order.executor_id).first()
        if not executor:
            raise ValueError(f"Исполнителем должен быть Работник привязанным к 'Заказу'")

        db_visit = ModelVisit(shop_id=shop_id,
                              author_id=author_id,
                              executor_id=executor_id,
                              order_id=order_id,
                              created_at=created_at)
        db.session.add(db_visit)
        db.session.commit()
        return db_visit.id

    @strawberry.mutation
    async def update_visit(self,
                           phone_number_customer: str,
                           visit_id: int,
                           shop_id: int,
                           author_id: int,
                           executor_id: int,
                           order_id: int,
                           created_at: datetime = datetime.now()) -> str:

        customer = db.session.query(ModelCustomer).filter(ModelCustomer.phone_number == phone_number_customer).first()
        if not customer:
            raise ValueError(f"Такого заказчика не существует")

        shop = db.session.query(ModelShop).filter(shop_id == customer.shop_id).first()
        if not shop:
            raise ValueError(f"Заказчик может обновить заказ только на свою Торговую точку")

        author = db.session.query(ModelCustomer).filter(author_id == customer.id).first()
        if not author:
            raise ValueError(f"Автором может быть только текущий заказачик")

        order = db.session.query(ModelOrder).filter(order_id == ModelOrder.id).first()
        if not order:
            raise ValueError(f"Заказ не найден")
        if order.expiration_data.timestamp() < created_at.timestamp():
            raise ValueError(f"Срок 'Заказа' истек")

        executor = db.session.query(ModelEmployee).filter(executor_id == order.executor_id).first()
        if not executor:
            raise ValueError(f"Исполнителем должен быть Работник привязанным к 'Заказу'")

        visit_db = db.session.query(ModelVisit).filter(ModelVisit.id == visit_id).first()

        if visit_db:
            visit_db.shop_id = shop_id
            visit_db.author_id = author_id
            visit_db.executor_id = executor_id
            visit_db.created_at = created_at
            visit_db.order_id = order_id
            db.session.commit()

        if not visit_db:
            raise ValueError(f"Посещение не найдено")

        return f"Fields updated successfully"

    @strawberry.mutation
    async def delete_visit(self, phone_number_customer: str, visit_id: int) -> str:
        customer = db.session.query(ModelCustomer).filter(ModelCustomer.phone_number == phone_number_customer).first()
        if not customer:
            raise ValueError("Такого заказчика не существует")

        visit = db.session.query(ModelVisit).filter(visit_id == ModelVisit.id).first()
        if visit and visit.author_id == customer.id:
            db.session.delete(visit)
            db.session.commit()
            db.session.close()
        else:
            raise ValueError("Заказчик может удалить только свой посещения")
        return f"Object deleted successfully"
