from datetime import timedelta
from http import HTTPStatus
from flask import current_app, jsonify, request
from sqlalchemy.orm import Session, Query
from app.models.user_model import UserModel
from flask_jwt_extended import create_access_token, jwt_required

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
        user = UserModel(**data)

        session.add(user)
        session.commit()

    except:
        # depurar os tipos de erros; colocar nas exceptions fazer o pull.
        return {"error": "email já existe."}, HTTPStatus.CONFLICT

    return jsonify(user), HTTPStatus.CREATED


def login():
    session: Session = current_app.db.session
    data = request.get_json()

    data_2 = {
        "email": data["email"],
        "password_hash": data["password"]
    }

    user: UserModel = session.query(UserModel).filter_by(email=data_2["email"]).first()

    if not user:
       return {"error": "usuário não encontrado."}, HTTPStatus.NOT_FOUND

    if user.verify_password(data_2["password_hash"]):
        accessToken = create_access_token(identity=user, expires_delta=timedelta(minutes=60))
        return jsonify({"accessToken": accessToken}), HTTPStatus.OK
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



