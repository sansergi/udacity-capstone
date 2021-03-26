from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, URL


class ActorForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    age = IntegerField(
        'age', validators=[DataRequired()]
    )
    gender = SelectField(
        'gender', validators=[DataRequired()],
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female')
        ]
    )
    picture_link = StringField(
        'picture_link', validators=[URL()]
    )
    movie_id = IntegerField(
        'movie_id', validators=[DataRequired()]
    )


class MovieForm(FlaskForm):
    title = StringField(
        'title', validators=[DataRequired()]
    )
    release_date = DateField(
        'release_date', validators=[DataRequired()]
    )
    image_link = StringField(
        'image_link', validators=[URL()]
    )
