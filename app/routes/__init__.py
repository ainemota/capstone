from flask import Blueprint
from app.routes.rooms_blueprint import bp_rooms
from app.routes.categories_blueprint import bp_categories
from app.routes.products_blueprint import bp as bp_products
from app.routes.addresses_blueprint import bp as bp_addresses
from app.routes.users_blueprint import bp as bp_users


def init_app(app):
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_products)
    app.register_blueprint(bp_addresses)
    app.register_blueprint(bp_rooms)
    app.register_blueprint(bp_categories)
