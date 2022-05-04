from http import HTTPStatus

from flask_jwt_extended import jwt_required, get_jwt_identity

from app.configs.database import db
from flask import request, jsonify
from sqlalchemy.orm import Session

from app.models.category_model import CategoryModel
from app.models.room_model import RoomModel
from app.models.address_model import Address
from app.exceptions.InvalidId import InvalidId

from ipdb import set_trace

from app.models.rooms_categories_model import RoomsCategoriesModel


@jwt_required()
def post_room():
    data = request.get_json()
    user_id = get_jwt_identity()
    session: Session = db.session()

    try:
        room = RoomModel(
            title=data["title"],
            description=data["description"],
            status=data["status"],
            locator_id=user_id["id"],
        )

        is_available = (
            session.query(RoomModel).filter(RoomModel.title == room.title).first()
        )

        if is_available:
            return {"error": "Name already exists"}

        address = Address(
            CEP=data["address"]["CEP"], number=data["address"]["number"], complement=data["address"]["complement"]
        )

        address.create()
        room.address_id = address.id
        room.create()

        if "categories" in data:
            for category in data["categories"]:
                category_database = session.query(CategoryModel).filter(CategoryModel.name == category).first()

                if not category_database:
                    category_database = CategoryModel(name=category, description="")
                    category_database.create()

                rooms_categories = RoomsCategoriesModel(category_id=category_database.id, rooms_id=room.id)
                rooms_categories.create()

        return jsonify(room), HTTPStatus.CREATED

    except KeyError:
        return {
            "error": "You must pass correct keys",
            "body_request": {
                "title": "",
                "description": "",
                "address": {"CEP": "", "number": "", "complement": ""},
                "status": True,
            },
        }, HTTPStatus.BAD_REQUEST


@jwt_required()
def get_room():
    session = db.session()
    rooms = session.query(RoomModel).all()

    return jsonify(rooms), HTTPStatus.OK


@jwt_required()
def patch_room(room_id):
    data = request.get_json()
    user = get_jwt_identity()
    session: Session = db.session()

    try:
        room = session.query(RoomModel).get(room_id)
        if not room:
            raise InvalidId(modelName="Room")

    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND

    address = session.query(Address).get(room.address_id)

    if str(room.locator_id) != user["id"]:
        return {"error": "you need to be the owner"}

    if "title" in data:
        is_available = (
            session.query(RoomModel).filter(RoomModel.title == data["title"]).first()
        )
        if is_available:
            return {"error": "Name already exists"}

    room.update(data)
    room.create()
    address.update(data["address"], address)
    address.create()

    return jsonify(room), HTTPStatus.OK


@jwt_required()
def delete_room(room_id):
    user = get_jwt_identity()
    session: Session = db.session()

    try:
        room = session.query(RoomModel).get(room_id)
        if not room:
            raise InvalidId(modelName="Room")

    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND

    address = session.query(Address).get(room.address_id)

    room.is_the_owner(user)

    session.delete(room)
    session.commit()
    session.delete(address)
    session.commit()

    return "", HTTPStatus.NO_CONTENT


@jwt_required()
def get_by_id_room(room_id):
    session: Session = db.session()

    try:
        room = session.query(RoomModel).get(room_id)
        if not room:
            raise InvalidId(modelName="Room")

    except InvalidId as e:
        return e.message, HTTPStatus.NOT_FOUND

    return jsonify(room), HTTPStatus.OK
