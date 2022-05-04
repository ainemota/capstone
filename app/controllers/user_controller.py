from datetime import timedelta
from http import HTTPStatus
from flask import current_app, jsonify, request
from sqlalchemy.orm import Session, Query
from app.exceptions.AlreadyExists import AlreadyExists
from app.models.address_model import Address
from app.models.user_model import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash


@jwt_required()
def get_all_users():
    session: Session = current_app.db.session

    user = session.query(UserModel).all()

    if not user:
        return [], HTTPStatus.OK

    return jsonify(user), HTTPStatus.OK


def retrive():
    session: Session = current_app.db.session
    data = request.get_json()

    try:
        UserModel.validate_email(data)
        
        if type(data['address']) == dict:
            data = UserModel.create_user_address(data)
        else:
            address_id = data.pop("address")
            data['address_id'] = address_id

    except AlreadyExists as e:
        return e.message, HTTPStatus.CONFLICT

    user = UserModel(**data)
    session.add(user)
    session.commit()
    
    return jsonify(user), HTTPStatus.CREATED


def login():
    session: Session = current_app.db.session
    data = request.get_json()

    user: UserModel = session.query(UserModel).filter_by(email=data["email"]).first()

    if not user:
        return {"error": "usuário não encontrado."}, HTTPStatus.NOT_FOUND

    if user.verify_password(data["password"]):
        accessToken = create_access_token(identity=user, expires_delta=timedelta(minutes=60))
        return {"accessToken": accessToken}, HTTPStatus.OK
    else:
        return {"error": "Email ou Senha inválidos!"}, HTTPStatus.UNAUTHORIZED


@jwt_required()
def put_users(id: int):
    session: Session = current_app.db.session
    data: dict = request.get_json()
    
    try:
        user = session.query(UserModel).get(id)

        for key, value in data.items():
            setattr(user, key, value)

        session.commit()
    
    except AttributeError:
        return {"error": "usuário nao encontrado!"}, HTTPStatus.NOT_FOUND

    if not user:
        return {"error": "usuário não encontrado!"}, HTTPStatus.NOT_FOUND

    return jsonify(user), HTTPStatus.OK


@jwt_required()
def delete_user(id: int):
    session: Session = current_app.db.session

    user = session.query(UserModel).get(id)

    if not user:
        return {"error": "usuário não encontrado!"}, HTTPStatus.NOT_FOUND

    session.delete(user)
    session.commit()

    return {"msg": f"user {user.name} foi deletado!"}, HTTPStatus.OK


@jwt_required
def get_self_user():
    self_id = get_jwt_identity()

    self = UserModel.query.get(self_id)

    return {"self_user": self}, HTTPStatus.OK
