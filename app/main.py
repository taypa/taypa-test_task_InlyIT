from fastapi import FastAPI
from app.database.db import Base, engine
from app.basket.basket import router as router_basket
from app.add.add import add_router

def create_tables():
    Base.metadata.create_all(bind=engine)
    

def start():
    app = FastAPI()
    create_tables()
    return app

app = start()

@app.get("/")
def home_page():
    return {"message": "Микросервис для тестового задания InlyIT"}

app.include_router(router_basket)
app.include_router(add_router)
