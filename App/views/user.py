from flask import Blueprint, render_template
from flask_login import current_user, login_required

user_views = Blueprint('user_views', __name__, template_folder='../templates')


@user_views.route('/me', methods=['GET'])
@login_required
def get_locations():  # Should probably have a place where the user can edit their profile
    return render_template('user_profile.html', user=current_user)


@user_views.route('/locations', methods=['GET'])
@login_required
def get_locations():
    return render_template('locations.html', locations=current_user.locations)


@user_views.route('/notifications', methods=['GET'])
@login_required
def get_locations():
    return render_template('notifications.html', notifications=current_user.received_notifications)


@user_views.route('/following', methods=['GET'])
@login_required
def get_locations():
    return render_template('following.html', following=current_user.following)
