from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, URL


class AddForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    map_url = StringField(label="Map URL", validators=[DataRequired()])
    img_url = StringField(label="Image URL", validators=[DataRequired()])
    location = StringField(label="Location", validators=[DataRequired()])
    seats = StringField(label="Seats", validators=[DataRequired()])
    has_toilet = SelectField(label="Toilet", validators=[DataRequired()], choices=["YES", "NO"])
    has_wifi = SelectField(label="Wifi", validators=[DataRequired()], choices=["YES", "NO"])
    has_sockets = SelectField(label="Sockets", validators=[DataRequired()], choices=["YES", "NO"])
    can_take_calls = SelectField(label="Take Calls", validators=[DataRequired()], choices=["YES", "NO"])
    coffee_price = StringField(label="Coffee Price")
    submit = SubmitField("Submit")
