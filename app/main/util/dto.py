from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operation')
    user = api.model(
        'user',
        {
            'email': fields.String(required=True, description='user email address'),
            'firstname': fields.String(required=True, description='user firstname'),
            'lastname': fields.String(required=True, description='user lastname'),
            'password': fields.String(required=True, description='user password'),
            'role_id': fields.Integer(required=True, description='user\'s role'),
            'public_id': fields.String(description='user Identifier'),
        },
    )
