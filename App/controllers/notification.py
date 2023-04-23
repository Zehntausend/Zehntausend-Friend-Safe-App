from App.database import db
from App.models import Notification


def create_notification(type, user_id, target_user_id):
    new_notification = Notification(type=type, user_id=user_id, target_user_id=target_user_id)
    db.session.add(new_notification)
    db.session.commit()
    return new_notification


def get_notification_by_id(notification_id):
    return Notification.query.get(notification_id)


def get_notifications_by_user_id(user_id):
    return Notification.query.filter_by(user_id=user_id).all()


def delete_notification(notification):
    db.session.delete(notification)
    db.session.commit()


def get_notifications_json(notifications):
    if not notifications:
        return []
    notifications = [notification.get_json() for notification in notifications]
    return notifications
