from flask import Blueprint
from app.routes.products_blueprint import bp as bp_products

def init_app(app):
    # registrar todas as blueprints criadas importando-as
    app.register_blueprint(bp_products)