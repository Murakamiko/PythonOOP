from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class AccountTransfertForm(FlaskForm):    
    name = StringField("name", validators=[DataRequired()])
    firstname = StringField("firstname", validators=[DataRequired()])
    password = IntegerField("password", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    userdescription("user description",validators=[DataRequired()])