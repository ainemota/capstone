from flask import Blueprint
from app.controllers.product_controller import create, delete, products, update, specific, available

bp = Blueprint("bp_products", __name__, url_prefix="/products")

bp.post("")(create)
bp.get("")(products)
bp.get("/available")(available)
bp.get("/<product_id>")(specific)
bp.patch("/<product_id>")(update)
bp.delete("/<product_id>")(delete)
