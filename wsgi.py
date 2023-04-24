from App.controllers import create_user
from App.extensions import db, Migrate
from App.main import create_app
from App.models import Follow

app = create_app()
migrate = Migrate(app, db)

@app.cli.command("init")
def initialize():
    db.drop_all()
    db.create_all()

    bob = create_user(username='bob', password='bobpass', display_name='Bob Smith', email='bob@gmail.com')
    alice = create_user(username='alice', password='alicepass', display_name='Alice Johnson', email='alice@gmail.com')
    charlie = create_user(username='charlie', password='charliepass', display_name='Charlie Brown', email='charlie@gmail.com')

    new_follow1 = Follow(user_id=alice.id, target_user_id=bob.id)
    new_follow2 = Follow(user_id=charlie.id, target_user_id=bob.id)

    db.session.add(new_follow1)
    db.session.add(new_follow2)
    db.session.commit()

    print(bob.get_json())

    # Get Bob's followers
    followers = bob.followers.all()

    # Print the list of followers
    print("Bob's followers:")
    for follow in followers:
        print(follow.follower.username)