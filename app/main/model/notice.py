from .. import db


class Notice(db.model):
    __tablename__ = 'notice'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    wine_id = db.Column(db.Integer, db.ForeignKey('wine.id'))
    description = db.Column(db.String)
    date = db.Column(db.Date)
