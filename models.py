from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db_conf import Base
import uuid, enum
from sqlalchemy.orm import backref


class Shop(Base):
    __tablename__ = "shop"
    id = Column(Integer, primary_key=True)
    title = Column(String)


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    phone_number = Column(String(255), unique=True)
    shop_id = Column(Integer, ForeignKey('shop.id'), nullable=False)
    shop = relationship("Shop", backref=backref("employee", cascade="all,delete"))


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    phone_number = Column(String(255), unique=True)
    shop_id = Column(Integer, ForeignKey('shop.id'), nullable=False)
    shop = relationship("Shop", backref=backref("customer", cascade="all,delete"))


class OrderStatusEnum(enum.Enum):
    started = 'started'
    ended = 'ended'
    in_process = 'in process'
    awaiting = 'awaiting'
    canceled = 'canceled'


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.started)

    shop_id = Column(Integer, ForeignKey('shop.id'), nullable=False)
    shop = relationship("Shop", backref=backref("order", cascade="all,delete"))

    author_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    author = relationship("Customer", backref=backref("order", cascade="all,delete"))

    executor_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    executor = relationship("Employee", backref=backref("order", cascade="all,delete"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    expiration_data = Column(DateTime(timezone=True), onupdate=func.now())

    visit = relationship('Visit', back_populates='order', uselist=False)


class Visit(Base):
    __tablename__ = "visit"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    executor_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    executor = relationship("Employee", backref=backref("visit", cascade="all,delete"))

    author_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    author = relationship("Customer", backref=backref("visit", cascade="all,delete"))

    shop_id = Column(Integer, ForeignKey('shop.id'), nullable=False)
    shop = relationship("Shop", backref=backref("visit", cascade="all,delete"))

    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship("Order", back_populates='visit')
