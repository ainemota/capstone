from flask import Blueprint
from app.controllers.product_controller import create_product

bp = Blueprint("bp_products", __name__, url_prefix="/products")

bp.post("")(create_product)
