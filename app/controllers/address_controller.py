from http import HTTPStatus
from flask import request
from app.exceptions.InvalidKeys import InvalidKeys
from app.models.address_model import Address


def create_address():
    data = request.get_json()

    try:
        Address.validate_keys(data)
    except InvalidKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST

    new_address = Address(**data)
    new_address.create()

    return {"address_created": new_address}, HTTPStatus.CREATED
