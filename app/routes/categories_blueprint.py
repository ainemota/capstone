from flask import Blueprint
from app.controllers.category_controller import (
    post_category,
    get_category,
    patch_category,
    delete_category,
    get_by_name_category,
)


bp_categories = Blueprint("categories", __name__, url_prefix="/categories")

bp_categories.post("")(post_category)
bp_categories.get("")(get_category)
bp_categories.patch("/<category_id>")(patch_category)
bp_categories.delete("/<category_id>")(delete_category)
bp_categories.get("/<name>")(get_by_name_category)
