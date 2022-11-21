from pydantic import BaseModel
from typing import Optional, Union
from pydantic import BaseModel, validator, Field
from datetime import datetime, time, timedelta
from fastapi import Body

from models import OrderStatusEnum, Visit
from models import Shop


class ShopSchema(BaseModel):
    title: str

    class Config:
        orm_mode = True


# class ShopModel(SQLAlchemyObjectType):
#     class Meta:
#         model = Shop


class Employee(BaseModel):
    name: str = Field(max_length=255)
    phone_number: str = Field(max_length=255)
    shop_id: int

    class Config:
        orm_mode = True


class Customer(BaseModel):
    name: str = Field(max_length=255)
    phone_number: str = Field(max_length=255)
    shop_id: int

    class Config:
        orm_mode = True


class BaseOrder(BaseModel):
    status: Optional[OrderStatusEnum]
    shop_id: int
    author_id: int
    executor_id: int
    created_at: Union[datetime, None] = Body(default=datetime.now())
    expiration_data: Union[datetime, None] = Body(default=datetime.now())

    class Config:
        orm_mode = True


class BaseVisit(BaseModel):
    shop_id: int
    author_id: int
    executor_id: int
    order_id: int
    created_at: Union[datetime, None] = Body(default=datetime.now())

    class Config:
        orm_mode = True


class StatusOrder(BaseModel):
    status: Optional[OrderStatusEnum]

    class Config:
        orm_mode = True
