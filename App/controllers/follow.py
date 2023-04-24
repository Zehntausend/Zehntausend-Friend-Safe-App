# from App.extensions import db
# from App.models import Follow

from App.models.follow import *

def create_follow(user_id, target_user_id):
    new_follow = Follow(user_id=user_id, target_user_id=target_user_id)
    db.session.add(new_follow)
    db.session.commit()
    return new_follow


def get_follow_by_id(follow_id):
    return Follow.query.get(follow_id)


def get_follows_by_user_id(user_id):
    return Follow.query.filter_by(user_id=user_id).all()


def get_followers_by_user_id(user_id):
    return Follow.query.filter_by(target_user_id=user_id).all()


def delete_follow(follow):
    db.session.delete(follow)
    db.session.commit()


def get_follows_json(follows: list):
    if not follows:
        return []
    follows = [follow.get_json() for follow in follows]
    return follows
