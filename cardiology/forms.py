from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, DateField, IntegerField, SelectField, \
    FloatField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, NumberRange
from cardiology.models import Patients, Doctors, Admins
from flask_login import current_user
from flask import session


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        patientName = Patients.query.filter_by(p_username=username_to_check.data).first()
        if patientName:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_address_to_check):
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
        validators=[NumberRange(min=1000000000, max=10000000000, message="Please enter a valid phone number"),
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


class addDoctorForm(FlaskForm):

    def validate_username(self, username_to_check):
        doctorName = Doctors.query.filter_by(d_username=username_to_check.data).first()
        if doctorName:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_address_to_check):
        doctorEmail = Doctors.query.filter_by(d_email=email_address_to_check.data).first()
        if doctorEmail:
            raise ValidationError('Email Address already exists! Please try a different email address')

    def validate_phone(self, phone_to_check):
        doctorPhone = Doctors.query.filter_by(d_phone=phone_to_check.data).first()
        if doctorPhone:
            raise ValidationError('Phone number already exists! Please try a different phone number')

    # To create all combinations of hours
    def work_period_counter(self):
        l1 = []
        l2 = []
        for x in range(24):
            if x <= 9:
                l1.append(f"{self} 0{x}:00")
                l2.append(f"0{x}:00")
            else:
                l1.append(f"{self} {x}:00")
                l2.append(f"{x}:00")
        return list(zip(l1, l2))

    username = StringField(validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField(validators=[DataRequired(), Length(min=6)])
    fullname = StringField(validators=[Length(min=2, max=50), DataRequired()])
    email = StringField(validators=[Email(), DataRequired()])
    phone = IntegerField(
        validators=[NumberRange(min=1000000000, max=10000000000, message="Please enter a valid phone number"),
                    DataRequired()])
    birthdate = DateField(validators=[DataRequired()])
    sex = RadioField(choices=[('Male', 'Male'), ('Female', 'Female')], validators=[DataRequired()])
    salary = FloatField(validators=[DataRequired(), NumberRange(min=2000, max=100000000)])
    work_periodFrom = SelectField(label="NEW WORK PERIOD", validators=[DataRequired()],
                                  choices=work_period_counter('From'))
    work_periodTo = SelectField(validators=[DataRequired()], choices=work_period_counter('To'))
    position = SelectField(validators=[DataRequired()], choices=[('Medical Interns', 'Medical Interns'),
                                                                 ('Resident Medical Officer',
                                                                  'Resident Medical Officer'),
                                                                 ('Medical Trainee Registrar',
                                                                  'Medical Trainee Registrar'),
                                                                 ('Consultant', 'Consultant'),
                                                                 ('Head of Department', 'Head of Department')])

    submit = SubmitField(label='Add Doctor')


class editDoctorForm_foreign(FlaskForm):

    def validate_username(self, username_to_check):

        updatedDoctor = Doctors.query.filter_by(d_id=int(session['doc_id'])).first()
        doctorName = Doctors.query.filter_by(d_username=username_to_check.data).first()
        if doctorName and not (updatedDoctor.d_id == doctorName.d_id):
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_address_to_check):
        updatedDoctor = Doctors.query.filter_by(d_id=int(session['doc_id'])).first()
        doctorEmail = Doctors.query.filter_by(d_email=email_address_to_check.data).first()
        if doctorEmail and not (updatedDoctor.d_id == doctorEmail.d_id):
            raise ValidationError('Email Address already exists! Please try a different email address')

    def validate_phone(self, phone_to_check):
        updatedDoctor = Doctors.query.filter_by(d_id=int(session['doc_id'])).first()
        doctorPhone = Doctors.query.filter_by(d_phone=phone_to_check.data).first()
        if doctorPhone and not (updatedDoctor.d_id == doctorPhone.d_id):
            raise ValidationError('Phone number already exists! Please try a different phone number')
    # To create all combinations of hours
    def work_period_counter(self):
        l1 = []
        l2 = []
        for x in range(24):
            if x <= 9:
                l1.append(f"{self} 0{x}:00")
                l2.append(f"0{x}:00")
            else:
                l1.append(f"{self} {x}:00")
                l2.append(f"{x}:00")
        return list(zip(l1, l2))

    password = PasswordField(validators=[DataRequired(), Length(min=6)])
    email = StringField(validators=[Email(), DataRequired()])
    phone = IntegerField(
        validators=[NumberRange(min=1000000000, max=10000000000, message="Please enter a valid phone number"),
                    DataRequired()])
    salary = FloatField(validators=[DataRequired(), NumberRange(min=2000, max=100000000)])
    work_periodFrom = SelectField(validators=[DataRequired()],
                                  choices=work_period_counter('From'))
    work_periodTo = SelectField(validators=[DataRequired()], choices=work_period_counter('To'))
    position = SelectField(validators=[DataRequired()],
                           choices=[('Medical Interns', 'Medical Interns'),
                                    ('Resident Medical Officer',
                                     'Resident Medical Officer'),
                                    ('Medical Trainee Registrar',
                                     'Medical Trainee Registrar'),
                                    ('Consultant', 'Consultant'),
                                    ('Head of Department', 'Head of Department')])
    submit = SubmitField(label='Update Doctor')


class addAdminForm(FlaskForm):
    def validate_username(self, username_to_check):
        adminName = Admins.query.filter_by(a_username=username_to_check.data).first()
        if adminName:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_address_to_check):
        adminEmail = Admins.query.filter_by(a_email=email_address_to_check.data).first()
        if adminEmail:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField(validators=[DataRequired(), Length(min=6)])
    fullname = StringField(validators=[Length(min=2, max=50), DataRequired()])
    email = StringField(validators=[Email(), DataRequired()])
    submit = SubmitField(label='Add Admin')


class editAdminForm(FlaskForm):
    def validate_email(self, email_address_to_check):
        updatedAdmin = Admins.query.get(current_user.a_id)
        adminEmail = Admins.query.filter_by(a_email=email_address_to_check.data).first()
        if adminEmail and not (updatedAdmin.a_id == adminEmail.a_id):
            raise ValidationError('Email Address already exists! Please try a different email address')

    password = PasswordField(validators=[DataRequired(), Length(min=6)])
    fullname = StringField(validators=[Length(min=2, max=50), DataRequired()])
    email = StringField(validators=[Email(), DataRequired()])
    submit = SubmitField(label='Update Admin')


class editPatientForm(FlaskForm):

    def validate_username(self, username_to_check):
        updatedPatient = Patients.query.get(current_user.p_id)
        patientName = Patients.query.filter_by(p_username=username_to_check.data).first()
        if patientName and not (updatedPatient.p_id == patientName.p_id):
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_address_to_check):
        updatedPatient = Patients.query.get(current_user.p_id)
        patientEmail = Patients.query.filter_by(p_email=email_address_to_check.data).first()
        if patientEmail and not (updatedPatient.p_id == patientEmail.p_id):
            raise ValidationError('Email Address already exists! Please try a different email address')

    def validate_phone(self, phone_to_check):
        updatedPatient = Patients.query.get(current_user.p_id)
        patientPhone = Patients.query.filter_by(p_phone=phone_to_check.data).first()
        if patientPhone and not (updatedPatient.p_id == patientPhone.p_id):
            raise ValidationError('Phone number already exists! Please try a different phone number')

    username = StringField(validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField(validators=[Email(), DataRequired()])
    phone = IntegerField(
        validators=[NumberRange(min=1000000000, max=10000000000, message="Please enter a valid phone number"),
                    DataRequired()])
    password = PasswordField(validators=[DataRequired(), Length(min=6)])
    submit = SubmitField(label='Update Patient')


class editDoctorForm_primary(FlaskForm):
    def validate_username(self, username_to_check):
        updatedDoctor = Doctors.query.get(current_user.d_id)
        doctorName = Doctors.query.filter_by(d_username=username_to_check.data).first()
        if doctorName and not (updatedDoctor.d_id == doctorName.d_id):
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email(self, email_address_to_check):
        updatedDoctor = Doctors.query.get(current_user.d_id)
        doctorEmail = Doctors.query.filter_by(d_email=email_address_to_check.data).first()
        if doctorEmail and not (updatedDoctor.d_id == doctorEmail.d_id):
            raise ValidationError('Email Address already exists! Please try a different email address')

    def validate_phone(self, phone_to_check):
        updatedDoctor = Doctors.query.get(current_user.d_id)
        doctorPhone = Doctors.query.filter_by(d_phone=phone_to_check.data).first()
        if doctorPhone and not (updatedDoctor.d_id == doctorPhone.d_id):
            raise ValidationError('Phone number already exists! Please try a different phone number')

    username = StringField(validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField(validators=[Email(), DataRequired()])
    phone = IntegerField(
        validators=[NumberRange(min=1000000000, max=10000000000, message="Please enter a valid phone number"),
                    DataRequired()])
    password = PasswordField(validators=[DataRequired(), Length(min=6)])
    submit = SubmitField(label='Update Doctor')
