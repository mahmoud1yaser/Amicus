from cardiology import db, bcrypt, login_manager
from flask_login import UserMixin
from flask import session


@login_manager.user_loader
def user_loader(id):
    if session["role"] == "Patient":
        return Patients.query.get(int(id))
    if session["role"] == "Doctor":
        return Doctors.query.get(int(id))
    if session["role"] == "Admin":
        return Admins.query.get(int(id))


class Doctors(db.Model, UserMixin):
    d_id = db.Column(db.Integer(), primary_key=True)
    d_username = db.Column(db.String(length=30), nullable=False, unique=True)
    d_password = db.Column(db.String(length=150), nullable=False)
    d_name = db.Column(db.String(), nullable=False)
    d_email = db.Column(db.String(length=50), nullable=False, unique=True)
    d_phone = db.Column(db.String(length=11), nullable=False, unique=True)
    d_birth_date = db.Column(db.Date(), nullable=False)
    d_sex = db.Column(db.String(), nullable=False)
    d_salary = db.Column(db.Float())
    d_workperiod = db.Column(db.String())
    d_position = db.Column(db.String())
    d_photo = db.Column(db.String(), default='../static/images/profile.png')

    def get_id(self):
        return self.d_id

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.d_password = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.d_password, attempted_password)


class Admins(db.Model, UserMixin):
    a_id = db.Column(db.Integer(), primary_key=True)
    a_username = db.Column(db.String(length=30), nullable=False, unique=True)
    a_password = db.Column(db.String(length=60), nullable=False)
    a_name = db.Column(db.String(), nullable=False)
    a_email = db.Column(db.String(length=50), nullable=False, unique=True)
    a_photo = db.Column(db.String(), default='../static/images/profile.png')

    def get_id(self):
        return self.a_id

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.a_password = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.a_password, attempted_password)


class Patients(db.Model, UserMixin):
    p_id = db.Column(db.Integer(), primary_key=True)
    p_username = db.Column(db.String(length=30), nullable=False, unique=True)
    p_password = db.Column(db.String(length=60), nullable=False)
    p_name = db.Column(db.String(), nullable=False)
    p_email = db.Column(db.String(length=50), nullable=False, unique=True)
    p_phone = db.Column(db.String(length=11), nullable=False, unique=True)
    p_birth_date = db.Column(db.Date(), nullable=False)
    p_sex = db.Column(db.String(), nullable=False)
    p_photo = db.Column(db.String(), default='../static/images/profile.png')

    def get_id(self):
        return self.p_id

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.p_password = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.p_password, attempted_password)


class Appointments(db.Model):
    appointment_number = db.Column(db.Integer(), primary_key=True)
    p_id = db.Column(db.Integer(), db.ForeignKey('patients.p_id'))
    d_id = db.Column(db.Integer(), db.ForeignKey('doctors.d_id'))
    date = db.Column(db.Date(), nullable=False)
    Time = db.Column(db.Time(), nullable=False)


class Medical_records(db.Model):
    p_id = db.Column(db.Integer(), db.ForeignKey( 'patients.p_id'), primary_key=True)
    d_id = db.Column(db.Integer(), db.ForeignKey('doctors.d_id'))
    diseases_history = db.Column(db.String())
    restricted_drugs = db.Column(db.String())


class p_Messages(db.Model):
    msg_number = db.Column(db.Integer(), primary_key=True)
    p_id = db.Column(db.Integer(), db.ForeignKey('patients.p_id'))
    d_id = db.Column(db.Integer(), db.ForeignKey('doctors.d_id'))
    message = db.Column(db.String())
    msg_date = db.Column(db.DateTime())


class Prescription(db.Model):
    pres_number = db.Column(db.Integer(), primary_key=True)
    p_id = db.Column(db.Integer(), db.ForeignKey('patients.p_id'))
    d_id = db.Column(db.Integer(), db.ForeignKey('doctors.d_id'))
    diagnosis = db.Column(db.String(), nullable=False)
    drugs = db.Column(db.String(), nullable=False)
    pres_date = db.Column(db.Date())


class Scans(db.Model):
    scan_num = db.Column(db.Integer(), primary_key=True)
    p_id = db.Column(db.Integer(), db.ForeignKey('patients.p_id'))
    scan_path = db.Column(db.String(), nullable=False)
    scan_date = db.Column(db.DateTime())

class examin(db.Model):
    _index = db.Column(db.Integer(), primary_key=True)
    d_id = db.Column(db.Integer(), db.ForeignKey('doctors.d_id'))
    p_id = db.Column(db.Integer(), db.ForeignKey('patients.p_id'))