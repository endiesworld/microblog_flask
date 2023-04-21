from datetime import datetime
from app import database as db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    body = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    def __repr__(self) -> str:
        return '<Post {}>'.format(self.body)