from app.main import db
from app.main.model.notice import Notice


def save_new_notice(data):
    notice = Notice.query.filter_by(
        user_id=data['user_id'], wine_id=data['wine_id']
    ).first()
    if not notice:
        new_notice = Notice(
            user_id=data['user_id'],
            wine_id=data['wine_id'],
            description=data['description'],
            date=data['date'],
        )
        save_changes(new_notice)
        response_object = {'status': 'success', 'message': 'Successfully registered'}
        return response_object, 201
    else:
        response_object = {'status': 'fail', 'message': 'Notice already exists'}
        return response_object, 409


def get_all_notices():
    return Notice.query.all()


def get_a_notice(id):
    return Notice.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
