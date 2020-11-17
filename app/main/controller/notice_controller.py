from flask import request
from flask_restplus import Resource, reqparse

from ..util.dto import NoticeDto
from ..service.notice_service import save_new_notice, get_a_notice, get_all_notices, delete

api = NoticeDto.api
_notice = NoticeDto.notice


@api.route('')
@api.route('?page=<page>&item=<item>')
@api.param('page', 'page indice')
@api.param('item', 'number of item per page')
class NoticeList(Resource):
    @api.doc('list_of_registered_notices')
    @api.marshal_list_with(_notice, envelope='data')
    def get(self):
        """List all registered notices"""
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, help='page indice')
        parser.add_argument('item', type=int, help='number of items per page')
        args = parser.parse_args()
        return get_all_notices(args)

    @api.response(201, 'Notice successfully created')
    @api.doc('create a new notice')
    @api.expect(_notice, validate=False)
    def post(self):
        """Creates a new notice"""
        data = request.json
        return save_new_notice(data=data)


@api.route('/<id>')
@api.param('id', 'The notice identifier')
@api.response(404, 'Notice not found')
class Notice(Resource):
    @api.doc('get a notice')
    @api.marshal_with(_notice)
    def get(self, id):
        """get a notice by its identifier"""
        notice = get_a_notice(id)
        if not notice:
            api.abort(404)
        else:
            return notice
    @api.doc('delete a notice')
    def delete(self, id):
        """delete a notice by id"""
        delete(id)