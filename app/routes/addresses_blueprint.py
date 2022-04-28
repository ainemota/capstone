from flask import Blueprint
from app.controllers.address_controller import addresses, create_address, update_address

bp = Blueprint("bp_addresses", __name__, url_prefix="/addresses")

bp.post("")(create_address)
bp.get("")(addresses)
bp.patch("/<address_id>")(update_address)