from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Book, Author, Publisher

# Connect to the activities database
engine = create_engine('sqlite:///activities.sqlite', echo=True)

# Create a session and add the people to the database
with Session(engine) as sess:
    persons = sess.query(Book).all()
    activities = sess.query(Author).all()
    locations = sess.query(Publisher).all()
