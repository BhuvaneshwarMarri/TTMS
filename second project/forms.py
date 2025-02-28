from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class CustomForm(FlaskForm):
    # value = StringField('value',validators=[DataRequired(message="Custom message: This field cannot be empty!")])
    # value = StringField('value',validators=[InputRequired(message="Custom message: This field cannot be empty!")],filters=[lambda x:f"Hello {x}",lambda x: f"Bye {x}"])
    # value = StringField('value',validators=[Length(min=10,max=20,message="length need to be between 10 and 20"),Optional()])
    # value = StringField('value',validators=[AnyOf(["success","failure"])])
    value = StringField('value',validators=[NoneOf(["success","failure"])])
    submit = SubmitField('submit')