from flask import request
from flask_restplus import Resource, reqparse

from ..util.dto import WineDto
from ..service.wine_service import save_new_wine, get_all_wines, get_a_wine, delete

api = WineDto.api
_wine = WineDto.wine

@api.route('/')
@api.route('?page=<page>&item=<item>')
@api.param('page', 'page indice')
@api.param('item', 'number of item per page')
class WineList(Resource):
    @api.doc('list_of_wine')
    @api.marshal_list_with(_wine, envelope='data')
    def get(self):
        """List all wines"""
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, help='page indice')
        parser.add_argument('item', type=int, help='number of items per page')
        
        args = parser.parse_args()
        return get_all_wines(args)
    
    @api.response(201, 'Wine successfully created')
    @api.doc('created a new wine')
    @api.expect(_wine, validate=True)
    def post(self):
        """Creates a new wine"""
        data = request.json
        return save_new_wine(data=data)


@api.route('/<id>')
@api.param('id', 'The wine identifier')
@api.response(404, 'Wine not found')
class Wine(Resource):
    @api.doc('get a wine')
    @api.marshal_with(_wine)
    def get(self, id):
        """get a wine by id"""
        wine = get_a_wine(id)
        if not wine: 
            api.abort(404)
        else:
            return wine
    @api.doc('delete a wine')
    def delete(self, id):
        """delete a wine by id"""
        delete(id)