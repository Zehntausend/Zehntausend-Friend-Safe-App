from App.database import db
from App.models import Location


def create_location(user_id, latitude, longitude, radius, tag):
    new_location = Location(user_id=user_id, latitude=latitude, longitude=longitude, radius=radius, tag=tag)
    db.session.add(new_location)
    db.session.commit()
    return new_location


def get_location_by_id(location_id):
    return Location.query.get(location_id)


def get_locations_by_user_id(user_id):
    return Location.query.filter_by(user_id=user_id).all()


def delete_location(location):
    db.session.delete(location)
    db.session.commit()


def get_locations_json(locations):
    if not locations:
        return []
    locations = [location.get_json() for location in locations]
    return locations
