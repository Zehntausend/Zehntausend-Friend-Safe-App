from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from App.extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    display_name = db.Column(db.String, nullable=False)  # User's real name
    home = db.Column(db.Boolean, nullable=False, default=True)  # Whether the user is home or not

    locations = db.relationship(
        "Location",
        backref="user",
        primaryjoin="User.id == Location.user_id",
        lazy="dynamic",
        cascade="delete"
    )
    followers = db.relationship(
        "Follow",
        backref="target_user",
        primaryjoin="User.id == Follow.target_user_id",
        lazy="dynamic",
        cascade="delete"
    )
    following = db.relationship(
        "Follow",
        backref="user",
        primaryjoin="User.id == Follow.user_id",
        lazy="dynamic",
        cascade="delete"
    )

    sent_notifications = db.relationship(
        "Notification",
        backref="user",
        primaryjoin="User.id == Notification.user_id",
        lazy="dynamic",
        cascade="delete"
    )

    received_notifications = db.relationship(
        "Notification",
        backref="target_user",
        primaryjoin="User.id == Notification.target_user_id",
        lazy="dynamic",
        cascade="delete"
    )

    sent_requests = db.relationship(
        "FollowRequest",
        backref="user",
        primaryjoin="User.id == FollowRequest.user_id",
        lazy="dynamic",
        cascade="delete"
    )

    received_requests = db.relationship(
        "FollowRequest",
        backref="target_user",
        primaryjoin="User.id == FollowRequest.target_user_id",
        lazy="dynamic",
        cascade="delete"
    )

    def get_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "display_name": self.display_name,
            "home": self.home,
        }

    def __init__(self, *, email, username, password, display_name):
        self.email = email
        self.username = username
        self.display_name = display_name
        self.set_password(password)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
