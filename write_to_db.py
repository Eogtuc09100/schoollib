from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Book, Author, Publisher

# Create some instances of the Person class
authors = [Author(first_name="Andrew", last_name="Dales",),
          Author(first_name="Chris", last_name="Brolin"),
          Author(first_name='Vera', last_name="Malcova"),
          Author(first_name='Daryl', last_name="Noyce"),
           Author(first_name='Elenora', last_name="Fontanesi")]

books = [Book(title="Lord of the Rings", ISBN_number="2421-12-212", num_pages=457, publication_date="10/12/1949", publisher_id=1),
Book(title="Advent of Code", ISBN_number="2221-12-212", num_pages=427, publication_date="10/2/1949", publisher_id=1),
Book(title="Animal Farm", ISBN_number="2421-12-212", num_pages=47, publication_date="10/12/1999", publisher_id=2),
         Book(title="1984", ISBN_number="3421-12-712", num_pages=327, publication_date="1/12/1984", publisher_id=2),
         Book(title="Animal Farm", ISBN_number="2421-12-22", num_pages=47, publication_date="10/12/1999", publisher_id=2),
         Book(title="Game of Thrones", ISBN_number="2891-12-212", num_pages=529, publication_date="11/11/2005", publisher_id=0)]

publishers = [Publisher(publisher_name="Penguin"), Publisher(publisher_name="Random House"), Publisher(publisher_name="Del Rey")]

books[0].authors.append(authors[2])
books[1].authors.append(authors[0])
books[1].authors.append(authors[4])
books[2].authors.append(authors[1])
books[3].authors.append(authors[1])
books[4].authors.append(authors[3])


# Connect to the activities database
engine = create_engine('sqlite:///library.sqlite', echo=True)

# Create a session and add the people to the database
with Session(engine) as sess:
    sess.add_all(books)
    sess.commit()
