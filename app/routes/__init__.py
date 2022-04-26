from flask import Blueprint
from app.routes.products_blueprint import bp as bp_products
from app.routes.addresses_blueprint import bp as bp_addresses
def init_app(app):
    # registrar todas as blueprints criadas importando-as
    app.register_blueprint(bp_products)
    app.register_blueprint(bp_addresses)