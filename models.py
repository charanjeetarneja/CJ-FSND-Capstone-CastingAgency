from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_utils import database_exists, create_database
from settings import DB_NAME, DB_USER, DB_PASSWORD
import datetime
import os
db = SQLAlchemy()

DATABASE_URI=os.environ.get("DATABASE_URL")

if DATABASE_URI is None:
    DATABASE_URI = "postgresql://{}:{}@{}/{}".format(DB_USER, DB_PASSWORD, 'localhost', DB_NAME)
else:
    DATABASE_URI=DATABASE_URI.replace("://", "ql://", 1) #fix for dialect correction to postgresql instead of postgres for compatibility with heroku

def setup_db(app, database_path=DATABASE_URI):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # create database if it doesnt already exists
    if not database_exists(DATABASE_URI):
        create_database(DATABASE_URI)

    db.app = app
    db.init_app(app)


def setup_migrations(app):
    migrate = Migrate(app, db)


def create_tables_for_test():
    db.drop_all()
    db.create_all()

class Actor(db.Model):
    __tablename__ = 'actors'  # set table name
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialized_actor(self):  # serialized actor data to return as json
        return (
            {"id": self.id,
             "name": self.name,
             "age": self.age,
             "gender": self.gender}
        )

    def __repr__(self):
        return f'Actor Details: {self.id}, {self.name}'


class Movie(db.Model):
    __tablename__ = 'movies'  # set table name
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    release_date = db.Column(db.Date(), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialized_movie(self):  # serialized movie data to return as json
        return {
                "id": self.id,
                "title": self.title,
                "release_date": self.release_date.isoformat()
                }
                

    def __repr__(self):
        return f'Movie details : {self.id} {self.title}'
