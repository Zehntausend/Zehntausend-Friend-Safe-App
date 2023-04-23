from App.controllers import create_user
from App.database import db, get_migrate
from App.main import create_app

app = create_app()
migrate = get_migrate(app)


@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()

    user=create_user(username='bob', password='bob', display_name='Bob Smith', email='bob@bobby.com')
    print(user.get_json())