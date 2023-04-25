from App.controllers import create_user
from App.extensions import db, Migrate
from App.main import create_app
from App.models import Follow
from App.models import FollowRequest

app = create_app()
migrate = Migrate(app, db)


@app.cli.command("init")
def initialize():
    db.drop_all()
    db.create_all()

    bob = create_user(username='bob', password='bobpass', display_name='Bob Smith', email='bob@gmail.com')
    alice = create_user(username='alice', password='alicepass', display_name='Alice Johnson', email='alice@gmail.com')
    charlie = create_user(username='charlie', password='charliepass', display_name='Charlie Brown', email='charlie@gmail.com')
    david = create_user(username='david', password='davidpass', display_name='David Lee', email='david@gmail.com')
    emily = create_user(username='emily', password='emilypass', display_name='Emily Davis', email='emily@gmail.com')

    charlie.home = False
    new_follow1 = Follow(user_id=alice.id, target_user_id=bob.id)
    new_follow2 = Follow(user_id=charlie.id, target_user_id=bob.id)
    new_follow3 = Follow(user_id=david.id, target_user_id=bob.id)
    new_follow4 = Follow(user_id=emily.id, target_user_id=bob.id)
    new_follow5 = Follow(user_id=bob.id, target_user_id=alice.id)
    new_follow6 = Follow(user_id=bob.id, target_user_id=charlie.id)

    newFollows1 = FollowRequest(user_id=bob.id, target_user_id=charlie.id, user_email = charlie.email, user_name = charlie.display_name)
    newFollows2 = FollowRequest(user_id=bob.id, target_user_id=alice.id, user_email = alice.email, user_name = alice.display_name)

    frank = create_user(username='frank', password='frankpass', display_name='Frank Johnson', email='frank@gmail.com')
    george = create_user(username='george', password='georgepass', display_name='George Brown', email='george@gmail.com')
    
    # Create new FollowRequest objects
    new_follow_request1 = FollowRequest(user_id=bob.id, target_user_id=frank.id, user_email = frank.email, user_name = frank.display_name)
    new_follow_request2 = FollowRequest(user_id=bob.id, target_user_id=george.id, user_email = george.email, user_name = george.display_name)
    
    # Add the new FollowRequest objects to the database
    db.session.add(new_follow_request1)
    db.session.add(new_follow_request2)
    db.session.add(new_follow1)
    db.session.add(new_follow2)
    db.session.add(new_follow3)
    db.session.add(new_follow4)
    db.session.add(new_follow5)
    db.session.add(new_follow6)
    db.session.add(newFollows1)
    db.session.add(newFollows2)
    db.session.commit()

    print(bob.get_json())

    # Get Bob's followers
    followers = bob.followers.all()

    # Print the list of followers
    print("Bob's followers:")
    for follow in followers:
        print(follow.follower.username)

    # Get the users that Bob is following
    following = bob.following.all()

    # Print the list of users that Bob is following
    print("Bob is following:")
    for follow in following:
        print(follow.target_user.username)