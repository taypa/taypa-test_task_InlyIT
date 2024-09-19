from sqlalchemy import Column,  Integer, String, ForeignKey

from .db import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String, unique=True)

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, unique=True)

class Cart(Base):
    __tablename__ = "cart"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer,  ForeignKey("user.id"))
    product_id = Column(Integer,  ForeignKey("product.id"))
    count = Column(Integer, nullable=False)