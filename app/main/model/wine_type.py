from .. import db


class WineType(db.Model):

    __tablename__ = 'wine_type'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String)
