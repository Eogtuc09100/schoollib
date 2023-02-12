from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Person, Activity, Location

# Connect to the activities database
engine = create_engine('sqlite:///activities.sqlite', echo=True)

# Create a session and add the people to the database
with Session(engine) as sess:
    persons = sess.query(Person).all()
    activities = sess.query(Activity).all()
    locations = sess.query(Location).all()
