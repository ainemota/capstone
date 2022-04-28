from flask import Blueprint
from app.controllers import user_controller


bp = Blueprint("users", __name__)


bp.get("/")(user_controller.get_all_users)
bp.post("/signup")(user_controller.retrive)
bp.post("/login")(user_controller.login)
bp.put("/<int:id>")(user_controller.put_users)
bp.delete("/<int:id>")(user_controller.delete_user)