from flask import request
from flask_restplus import Resource

from ..util.dto import NoticeDto
from ..service.notice_service import save_new_notice, get_a_notice, get_all_notices, delete

api = NoticeDto.api
_notice = NoticeDto.notice


@api.route('/')
class NoticeList(Resource):
    @api.doc('list_of_registered_notices')
    @api.marshal_list_with(_notice, envelope='data')
    def get(self):
        """List all registered notices"""
        return get_all_notices()

    @api.response(201, 'Notice successfully created')
    @api.doc('create a new notice')
    @api.expect(_notice, validate=True)
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