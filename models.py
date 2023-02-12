from sqlalchemy import Column, Integer, String, Table, UniqueConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime

# Base is called an Abstract Base Class - our SQL Alchemy models will inherit from this class
Base = declarative_base()

book_author = Table('book_author',
                        Base.metadata,
                        Column('id', Integer, primary_key=True),
                        Column('book_id', ForeignKey('book.id')),
                        Column('author_id', ForeignKey('author.id')),
                        UniqueConstraint('book_id', 'author_id')
                        )

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    ISBN_number = Column(String, nullable=False)
    num_pages = Column(Integer, nullable=False)
    publication_date = Column(String)
    publisher_id = Column(Integer, ForeignKey("publisher.id"), default=None)
    authors = relationship("Book",
                             secondary=book_author,
                             back_populates="author")

    def __repr__(self):
        return f"<Book({self.title})>"

class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    books = relationship("Book",
                              secondary=book_author,
                              back_populates="book")

    def __repr__(self):
        return f"<Author({self.first_name} {self.last_name})>"


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    publisher_name = Column(String, nullable=False)
    books = relationship("Author",
                              backref=backref("publisher"))

    def __repr__(self):
        return f"<Publisher({self.publisher_name})>"