from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class FollowRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    target_account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    
    
    account = db.relationship('Account', foreign_keys=[account_id], backref='sent_requests')
    target_account = db.relationship('Account', foreign_keys=[target_account_id], backref='received_requests')
