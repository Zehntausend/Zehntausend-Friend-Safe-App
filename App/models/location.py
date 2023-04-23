from geopy import distance

from App.database import db


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    radius = db.Column(db.Integer, nullable=False, default=50)  # Radius is defined in meters
    tag = db.Column(db.String, nullable=False)

    def __init__(self, user_id, latitude, longitude, radius, tag):
        self.user_id = user_id
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.tag = tag

    def get_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "radius": self.radius,
            "tag": self.tag,
        }

    def is_within_range(self, latitude, longitude):
        location_coords = (self.latitude, self.longitude)
        target_coords = (latitude, longitude)
        distance_meters = distance.distance(location_coords, target_coords).meters
        return distance_meters <= self.radius
