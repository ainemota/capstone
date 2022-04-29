from flask import Blueprint
from app.controllers.room_controller import post_room, get_by_id_room, patch_room, delete_room, get_room

bp_rooms = Blueprint("rooms", __name__, url_prefix="/rooms")

bp_rooms.post("")(post_room)
bp_rooms.get("")(get_room)
bp_rooms.patch("/<room_id>")(patch_room)
bp_rooms.delete("/<room_id>")(delete_room)
bp_rooms.get("/<room_id>")(get_by_id_room)
