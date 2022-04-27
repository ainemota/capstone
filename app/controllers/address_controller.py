from http import HTTPStatus
from flask import request
from app.models.address_model import Address


def create_address():
    data = request.get_json()

    new_address = Address(**data)
    new_address.create()

    return {"address_created": new_address}, HTTPStatus.CREATED
