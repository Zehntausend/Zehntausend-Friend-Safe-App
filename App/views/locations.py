from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from App.controllers import create_location

location_views = Blueprint('location_views', __name__, template_folder='../templates')


@location_views.route('/locations', methods=['POST'])
@login_required
def add_new_location():
    if request.method == "POST":
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        radius = request.form.get("radius")
        tag = request.form.get("tag")

        if not (latitude and longitude and tag):
            flash("Location must have at least a latitude, a longitude and a tag.")
            return redirect(url_for("locations"))

        location = create_location(latitude=latitude, longitude=longitude, radius=radius, tag=tag, user_id=current_user.id)
        return render_template('locations.html', locations=current_user.locations)
