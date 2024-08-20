from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    email = db.Column(db.String(120))
    celular = db.Column(db.String(20))
