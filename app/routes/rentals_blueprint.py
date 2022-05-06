from flask import Blueprint
from app.controllers.rental_controller import create_rental, user_rentals

bp=Blueprint("bp_rentals", __name__, url_prefix="/rentals")

bp.post("")(create_rental)
bp.get("")(user_rentals)