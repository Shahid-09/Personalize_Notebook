from app import db 
from datetime import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    username = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    _password = db.Column(db.String(150))
    notes = db.relationship('Note')

