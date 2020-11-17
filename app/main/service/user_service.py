import uuid

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            firstname=data['firstname'],
            lastname=data['lastname'],
            password=data['password'],
            role_id=data['role_id'],
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {'status': 'fail', 'message': 'User already exists'}
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(id):
    return User.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def delete(id):
    User.query.filter_by(id=id).delete()
    db.session.commit()

def generate_token(user):
    try:
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred.'
        }
        return response_object, 401