from .. import db


class Role(db.Model):

    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String)
