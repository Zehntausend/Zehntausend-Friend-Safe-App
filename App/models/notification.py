from datetime import datetime

from App.extensions import db


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    type = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    target_user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, type, user_id, target_user_id):
        self.type = type
        self.user_id = user_id
        self.target_user_id = target_user_id

    def get_json(self):
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "type": self.type,
            "user_id": self.user_id,
            "target_user_id": self.target_user_id,
        }
