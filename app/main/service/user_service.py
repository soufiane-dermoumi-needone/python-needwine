import uuid

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            firstname=data['firstname'],
            lastname=data['lastname'],
            password=data['password'],
            role_id=data['role_id'],
        )
        save_changes(new_user)
        response_object = {'status': 'success', 'message': 'Successfully registered'}
        return response_object, 201
    else:
        response_object = {'status': 'fail', 'message': 'User already exists'}
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
