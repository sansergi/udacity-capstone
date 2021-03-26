import os
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import Date


database_path = os.environ.get("DATABASE_URL")

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Movie(db.Model):

    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    release_date = db.Column(db.Date, nullable=False)
    image_link = db.Column(db.String(500))
    actors = db.relationship('Actor', backref='movies', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
            'image_link': self.image_link,
        }


class Actor(db.Model):

    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    picture_link = db.Column(db.String(500))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'),
                         nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
                'id': self.id,
                'name': self.name,
                'age': self.age,
                'gender': self.gender,
                'picture_link': self.picture_link,
                'movie_id': self.movie_id
            }
