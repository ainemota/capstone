from flask_sqlalchemy import SQLAlchemy
from environs import Env

db = SQLAlchemy()

env = Env()
env.read_env()


def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = env("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    db.init_app(app)
    app.db = db

    # importar todas as model para que as tabelas sejam criadas
