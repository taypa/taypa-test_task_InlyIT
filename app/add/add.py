from fastapi import APIRouter, HTTPException

from app.database.db import session
from app.database.models import User, Product

add_router = APIRouter(prefix='/add', tags=['Добавление пользователей и товаров'])

@add_router.get("/user", summary="Добавить пользователя")
def add_user(user:str):
    s = session()
    try:
        u = User(nickname=user)
        s.add(u)
        s.commit()
        return {"message": "Пользователь добавлен"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ошибка при добавлении пользователя")
    finally:
        s.close()

@add_router.get("/product", summary="Добавить товар")
def add_product(product:str):
    s = session()
    try:
        print(product)
        p = Product(product_name=product)
        s.add(p)
        s.commit()
        return {"message": "Товар добавлен"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)#"Ошибка при добавлении товара")
    finally:
        s.close()
