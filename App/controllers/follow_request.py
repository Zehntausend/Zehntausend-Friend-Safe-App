from App.database import db
from App.models import FollowRequest


def create_follow_request(user_id, target_user_id):
    new_request = FollowRequest(user_id=user_id, target_user_id=target_user_id)
    db.session.add(new_request)
    db.session.commit()
    return new_request


def get_follow_request_by_id(request_id):
    return FollowRequest.query.get(request_id)


def get_follow_requests_by_user_id(user_id):
    return FollowRequest.query.filter_by(user_id=user_id).all()


def get_follow_requests_by_target_user_id(user_id):
    return FollowRequest.query.filter_by(target_user_id=user_id).all()


def delete_follow_request(request):
    db.session.delete(request)
    db.session.commit()


def get_follow_requests_json(follow_requests):
    if not follow_requests:
        return []
    follow_requests = [follow_request.get_json() for follow_request in follow_requests]
    return follow_requests
