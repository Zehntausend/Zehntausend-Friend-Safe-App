from datetime import datetime

from App.extensions import db

class FollowRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    target_user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_email = db.Column(db.Integer, db.ForeignKey("user.email"), nullable=True)
    user_name = db.Column(db.String, db.ForeignKey("user.display_name"), nullable=True)
