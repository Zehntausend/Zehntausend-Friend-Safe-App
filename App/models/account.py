from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class Account(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    display_name = db.Column(db.String, nullable=False) # User's real name (e.g. Natan Karov)
    home = db.Column(db.Boolean, nullable=False, default=True) # Whether the user is home or not.

    locations = db.relationship("Location", back_populates="account")

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

