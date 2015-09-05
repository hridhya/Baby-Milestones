from app import app
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class LoginForm(Form) :
	openid = StringField('openid', validators=[DataRequired()])
	