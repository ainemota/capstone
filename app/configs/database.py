from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from environs import Env


db = SQLAlchemy()

env = Env()
env.read_env()


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = env("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = env("SECRET_KEY")
    app.config["JSON_SORT_KEYS"] = False
    db.init_app(app)
    app.db = db

    # inicializa as models
    from app.models.user_model import UserModel
    from app.models.address_model import Address
    from app.models.product_model import Product
    from app.models.room_model import RoomModel
    from app.models.category_model import CategoryModel
    from app.models.rooms_categories_model import RoomsCategoriesModel
