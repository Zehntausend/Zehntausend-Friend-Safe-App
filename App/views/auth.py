from flask import Blueprint, request, flash, redirect, url_for
from flask_login import login_required, login_user, logout_user
from flask import render_template
from flask import session

from App.controllers.user import create_user
from App.extensions import login_manager
from App.models import User

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

"""
@auth_views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Logged in successfully.")
            return redirect(url_for("homepage"))
        else:
            flash("Incorrect credentials.")
            return redirect(url_for("login"))
    else:
        # Handle GET requests here
        return render_template("login.html")
"""
@auth_views.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Logged in successfully.")
            session.pop('_flashes', None)  
            return redirect(url_for("user_views.get_user_profile"))
        else:
            print("Invalid login")
            flash("Incorrect credentials.")
            return redirect(url_for("auth_views.login"))
    else:
        session.pop('_flashes', None)  
        return render_template("login.html")

@auth_views.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth_views.login"))


from sqlalchemy.exc import IntegrityError

@auth_views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        display_name = request.form.get('display_name')
        
        # Check if the username already exists in the database
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            # The username already exists, display an error message to the user
            flash(f'The username {username} is already taken. Please choose a different username.')
        else:
            try:
                # The username is available, attempt to create a new user
                new_user = create_user(username=username, password=password, email=email, display_name=display_name)
                if new_user:
                    flash('Registration successful!')
                    return redirect(url_for('auth_views.login'))
                else:
                    flash('Registration failed.')
            except IntegrityError as e:
                # Handle any other database integrity errors
                flash(f'An error occurred: {e}')
    session.pop('_flashes', None)        
    return render_template('register.html')