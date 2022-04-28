from flask import Blueprint, Flask
from app.routes.users_blueprint import bp as bp_user
from app.routes.addresses_blueprint import bp as bp_addresses


bp_api = Blueprint("api", __name__)


def init_app(app: Flask):
    bp_api.register_blueprint(bp_user)
    app.register_blueprint(bp_api)
    app.register_blueprint(bp_addresses)