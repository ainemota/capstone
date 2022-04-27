from flask import Blueprint
from app.controllers import user_controller


bp = Blueprint("user", __name__, url_prefix="")


bp.get("")(user_controller.get_all_users)
bp.post("/signup")(user_controller.retrive)
bp.post("/signin")(user_controller.login)
bp.put("/<int:id>")(user_controller.put_users)
bp.delete("/<int:id>")(user_controller.delete_user)