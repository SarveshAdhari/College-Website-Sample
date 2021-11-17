from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from college.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',
                  validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(),Length(5,70)])
    confirm_password = PasswordField('Confirm Password',
                                    validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already exists.')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already exists.')



class LoginForm(FlaskForm):
    email = StringField('Email',
                           validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(),Length(5,70)])
    submit = SubmitField('Login')

class UpdateForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',
                  validators=[DataRequired(),Email()])
    submit = SubmitField('Update')

class RegisterComplaint(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired(),Length(min=5,max=40)])
    body = TextAreaField('Complaint Body',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')