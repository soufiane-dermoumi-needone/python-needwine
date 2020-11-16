from .. import db


class Wine(db.Model):

    __tablename__ = 'wine'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.String)
    type_id = db.Column(db.Integer, db.ForeignKey('wine_type.id'))
    name = db.Column(db.String)
    wine_type = db.relationship('WineType', foreign_keys='Wine.type_id')
