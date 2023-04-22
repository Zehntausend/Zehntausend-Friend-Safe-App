from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longititude = db.Column(db.Float, nullable=False)
    radius = db.Column(db.Integer, nullable=False, default=50) # Radius is defined in meters
    tag = db.Column(db.String, nullable=False)

    account = db.relationship("Account", back_populates="locations")
