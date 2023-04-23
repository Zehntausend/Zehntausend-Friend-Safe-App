from App.database import db
from App.models import User


def create_user(*, username, password, email, display_name):
    new_user = User(username=username, password=password, email=email, display_name=display_name)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()


def get_user(id):
    return User.query.get(id)


def get_all_users():
    return User.query.all()


def get_users_json(users):
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users


def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None


def get_all_users_json():
    users = get_all_users()
    return get_users_json(users)