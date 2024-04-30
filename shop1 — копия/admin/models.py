from shop1 import db
from shop1 import app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=True, nullable=False)
    profile = db.Column(db.String(180), unique=True, nullable=False,
    default='profile.jpg')

    def __repr__(self):
        return '<User %r>' % self.username

# изменение 1 вместо db.create_all() ,буду использовать
with app.app_context():
    db.create_all()