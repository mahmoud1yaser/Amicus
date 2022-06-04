from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, DateField, IntegerField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, NumberRange
from cardiology.models import Patients, Doctors, Admins


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        patientName = Patients.query.filter_by(p_username=username_to_check.data).first()
        if patientName:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        patientEmail = Patients.query.filter_by(p_email=email_address_to_check.data).first()
        if patientEmail:
            raise ValidationError('Email Address already exists! Please try a different email address')

    def validate_phone(self, phone_to_check):
        patientPhone = Patients.query.filter_by(p_phone=phone_to_check.data).first()
        if patientPhone:
            raise ValidationError('Phone number already exists! Please try a different phone number')

    fullname = StringField(validators=[Length(min=2, max=50), DataRequired()])
    username = StringField(validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(validators=[Email(), DataRequired()])
    phone = IntegerField(
        validators=[NumberRange(min=100000000, max=10000000000, message="Please enter a valid phone number"),
                    DataRequired()])
    password = PasswordField(validators=[Length(min=6), DataRequired()])
    confirm_password = PasswordField(validators=[EqualTo('password'), DataRequired()])
    birthdate = DateField(validators=[DataRequired()])
    sex = RadioField(choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField(validators=[DataRequired(), Length(min=6)])
    role = SelectField(choices=[('Patient', 'Patient'), ('Doctor', 'Doctor'), ('Admin', 'Admin')],
                       validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
