from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, declared_attr
from app.config import Settings

DATABASE_URL = Settings.URL

engine = create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    __abstract__=True
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}"
