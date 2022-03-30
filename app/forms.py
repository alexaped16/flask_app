from flask_wtf import FlaskForm
from wtforms import StringField, FormField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class RegisterPhoneForm(FlaskForm): 
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    address = TextAreaField('Mailing Address', validators=[DataRequired()])
    submit = SubmitField('Register')
