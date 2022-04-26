from flask import Blueprint
from app.controllers.address_controller import create_address

bp = Blueprint("bp_addresses", __name__, url_prefix="/addresses")

bp.post("")(create_address)