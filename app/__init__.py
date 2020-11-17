from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.wine_controller import api as wine_ns
from .main.controller.notice_controller import api as notice_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='FLASK RESTPLUS API NEEDWINE WITH JWT',
    version='1.0',
    description='api needwine',
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(wine_ns, path='/wine')
api.add_namespace(notice_ns, path='/notice')
api.add_namespace(auth_ns)