from .. import db


class Notice(db.Model):
    __tablename__ = 'notice'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    wine_id = db.Column(db.Integer, db.ForeignKey('wine.id'))
    description = db.Column(db.String)
    date = db.Column(db.Date)
    user = db.relationship('User', foreign_keys='Notice.user_id')
    wine = db.relationship('Wine', foreign_keys='Notice.wine_id')
