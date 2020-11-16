from app.main import db
from app.main.model.wine import Wine


def save_new_wine(data):
    wine = Wine.query.filter_by(year=data['year'], name=data['name']).first()
    if not wine:
        new_wine = Wine(
            year=data['year'],
            type_id=data['type_id'],
            name=data['name'],
        )
        save_changes(new_wine)
        response_object = {'status': 'success', 'message': 'Successfully registered'}
        return response_object, 201
    else:
        response_object = {'status': 'fail', 'message': 'Wine already exists'}
        return response_object, 409


def get_all_wines():
    return Wine.query.all()


def get_a_wine(id):
    return Wine.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
