from flask import Blueprint
from app.controllers.product_controller import create_product, delete_product, products, update_product, specific_product, available_products

bp = Blueprint("bp_products", __name__, url_prefix="/products")

bp.post("")(create_product)
bp.get("")(products)
bp.get("/available")(available_products)
bp.get("/<product_id>")(specific_product)
bp.patch("/<product_id>")(update_product)
bp.delete("/<product_id>")(delete_product)
