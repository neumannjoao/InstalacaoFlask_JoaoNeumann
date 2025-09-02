from flask_sqlalchemy import flask_sqlalchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), Unique=True, nulltable=False)
    