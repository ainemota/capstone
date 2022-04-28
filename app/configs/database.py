from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db


    #inicializa as models    
    from app.models.user_model import UserModel
    from app.models.address_model import Address