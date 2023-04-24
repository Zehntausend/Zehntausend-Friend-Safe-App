from App.controllers import create_user
from App.extensions import db, Migrate
from App.main import create_app

app = create_app()
migrate = Migrate(app, db)


@app.cli.command("init")
def initialize():
    db.drop_all()
    db.create_all()

    user = create_user(username='bob', password='bobpass', display_name='Bob Smith', email='bob@gmail.com')
    print(user.get_json())
