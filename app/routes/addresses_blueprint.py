from flask import Blueprint
from app.controllers.address_controller import addresses, create_address, specific_address, update_address, delete_address

bp = Blueprint("bp_addresses", __name__, url_prefix="/addresses")

bp.post("")(create_address)
bp.get("")(addresses)
bp.get("/<address_id>")(specific_address)
bp.patch("/<address_id>")(update_address)
bp.delete("/<address_id>")(delete_address)
