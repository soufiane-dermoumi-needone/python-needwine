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
            'role': {
                'id': fields.Integer(
                    attribute='role.id', required=True, description='role id'
                ),
                'label': fields.String(
                    attribute='role.label', required=True, description='role label'
                )
            },
        },
    )


class WineDto:
    api = Namespace('wine', description='wine related operation')
    wine = api.model(
        'wine',
        {
            'id': fields.Integer(required=True, description='wine id'),
            'year': fields.String(required=True, description='wine year'),
            'type': {
                'id': fields.Integer(
                    attribute='wine_type.id', required=True, description='wine type id'
                ),
                'label': fields.String(
                    attribute='wine_type.label', required=True, description='wine type label'
                )
            },
            'name': fields.String(required=True, description="wine name")
        },
    )


class NoticeDto:
    api = Namespace('notice', description='notice related operation')
    notice = api.model(
        'notice',
        {
            'user': {
                'id': fields.Integer(
                    attribute='user.id', required=True, description='user id'
                ),
                'email': fields.String(
                    attribute='user.email', required=True, description='user email'
                ),
                'firstname': fields.String(
                    attribute='user.firstname', required=True, description='user firstname'
                ),
                'lastname': fields.String(
                    attribute='user.lastname', required=True, description='user firstname'
                ),
            },
            'wine': {
                'id': fields.Integer(
                    attribute='wine.id', required=True, description='wine id'
                ),
                'name': fields.String(
                    attribute='wine.name', required=True, description='wine name'
                ),
                'type': {
                    'id': fields.Integer(
                        attribute='wine_type.id', required=True, description='wine type id'
                    ),
                    'label': fields.String(
                        attribute='wine_type.label', required=True, description='wine type label'
                    )
                },
                'year': fields.Integer(
                    attribute='wine.year', required=True, description='wine year'
                ),
            },
            'description': fields.String(
                required=True, description='notice description'
            ),
            'date': fields.Date(required=True, description='notice date')
        }
    )
