from flask import Blueprint
from app.controllers import user_controller


bp = Blueprint("users", __name__, url_prefix="/users")


bp.get("/")(user_controller.get_all_users)
bp.get("/self")(user_controller.get_self_user)
bp.post("/signup")(user_controller.retrive)
bp.post("/login")(user_controller.login)
bp.put("/<id>")(user_controller.put_users)
bp.delete("/<id>")(user_controller.delete_user)
