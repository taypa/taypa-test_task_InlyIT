from fastapi import APIRouter, HTTPException

from app.database.db import session
from app.database.models import User, Product, Cart

router = APIRouter(prefix='/basket', tags=['Работа с корзиной'])

@router.get("/products", summary="Получить все товары")
def get_products():
    try:
        res = session().query(Product).all()
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ошибка")

@router.get("/users", summary="Получить всех пользователей")
def get_users():
    try:
        res = session().query(User).all()
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ошибка")

@router.get("/cart", summary="Получить корзину")
def get_carts():
    try:
        res = session().query(Cart).all()
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ошибка")

def get_user_and_product(s, 
                         user_id:int, 
                         product_id: int):
    user = s.query(User).get(user_id)
    product = s.query(User).get(product_id)
    return user, product

@router.get("/add", summary="Добавить количество товаров в корзину")
def add(user_id: int,
        product_id: int,
        cnt: int):
    s = session()
    try:
        user, product = get_user_and_product(s, user_id, product_id)
        if user and product:
            cart_item = s.query(Cart).filter_by(user_id=user_id,\
                                                product_id=product_id).first()
            if cart_item:
                cart_item.count += cnt
            else:
                basket = Cart(user_id=user_id, product_id=product_id, count=cnt)
                s.add(basket)
            s.commit()
            return {"message": "Число товара увеличилось"}
        else:
            HTTPException(status_code=404, detail="Пользователь или товар не найден")
    except Exception as e:
        s.rollback()
        raise HTTPException(status_code=500, detail="Ошибка при добавлени")
    finally:
        s.close()

@router.get("/delete", summary="Удалить количество товара в корзине")
def delete(user_id: int,
           product_id: int):
    s = session()
    try:
        user, product = get_user_and_product(s, user_id, product_id)
        if user and product:
            cart_item = s.query(Cart).filter_by(user_id=user_id,\
                                                product_id=product_id).first()
            if cart_item:
                s.delete(cart_item)
                s.commit()
                return {"message": "Товар удален из корзины"}
            else:
                HTTPException(status_code=404, detail="Товар в корзине не найден")
    except Exception as e:
        s.rollback()
        raise HTTPException(status_code=500, detail="Ошибка при удалении")
    finally:
        s.close()

@router.get("/update", summary="Изменить количество товара в корзине")
def delete(user_id: int,
           product_id: int,
           cnt: int):
    s = session()
    try:
        user, product = get_user_and_product(s, user_id, product_id)
        if user and product:
            cart_item = s.query(Cart).filter_by(user_id=user_id,\
                                                product_id=product_id).first()
            if cart_item:
                cart_item.count = cnt
                s.commit()
                return {"message": "Число товара в корзине обновлено"}
            else:
                HTTPException(status_code=404, detail="Товар в корзине не найден")
    except Exception as e:
        s.rollback()
        raise HTTPException(status_code=500, detail="Ошибка при обновлении")
    finally:
        s.close()

