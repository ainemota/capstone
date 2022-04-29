from http import HTTPStatus

from flask_jwt_extended import jwt_required, get_jwt_identity

from app.configs.database import db
from flask import request, jsonify
from sqlalchemy.orm import Session

from app.models.room_model import RoomModel


@jwt_required()
def post_room():
    data = request.get_json()
    user_id = get_jwt_identity()

    room = RoomModel(
        title=data["title"],
        description=data["description"],
        status=data["status"],
        locator=user_id["id"]
    )

    with db.session() as session:
        session.add(room)
        session.commit()

    return jsonify(room), HTTPStatus.CREATED


@jwt_required()
def get_room():
    with db.session() as session:
        rooms = session.query(RoomModel).all()

    return jsonify(rooms), HTTPStatus.OK


@jwt_required()
def patch_room(room_id):
    data = request.get_json()

    with db.session() as session:
        session: Session

        room = session.query(RoomModel).get(room_id)

        for key, value in data.items():
            if not hasattr(room, key):
                continue
            setattr(room, key, value)

        session.add(room)
        session.commit()

    return jsonify(room), HTTPStatus.OK


@jwt_required()
def delete_room(room_id):
    with db.session() as session:
        session: Session

        room = session.query(RoomModel).get(room_id)
        session.delete(room)
        session.commit()

    return "", HTTPStatus.NO_CONTENT


@jwt_required()
def get_by_id_room(room_id):
    with db.session() as session:
        room = session.query(RoomModel).get(room_id)

    return jsonify(room), HTTPStatus.OK
