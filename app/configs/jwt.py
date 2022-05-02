from environs import Env
from flask import Flask
from flask_jwt_extended import JWTManager

env = Env()
env.read_env()


def init_app(app: Flask):
    app.config["JWT_SECRET_KEY"] = env("SECRET_KEY")
    JWTManager(app)
