from flask_wtf import FlaskForm
#imports the field types classes from wtforms library
from wtforms import StringField, PasswordField, BooleanField, SubmitField 
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    #for each form field, object of class of field type is created. First arg is for label Second arg is for checing that the field is not submitted empty

    username = StringField("Username", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

