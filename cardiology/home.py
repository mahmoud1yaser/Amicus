from flask import render_template, redirect, url_for, request, flash, Markup, session
from flask_sqlalchemy import SQLAlchemy
from cardiology.models import Doctors, Patients, Admins
from cardiology import app, db,  patient, admin
from cardiology.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required



@app.route('/')
def home_page():
    logout_user()
    session.clear()
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def register_page():
    session["role"]="Default"
    form = RegisterForm()
    if form.validate_on_submit():
        patient_to_create = Patients(p_username=form.username.data,
                                     p_name=form.fullname.data,
                                     p_email=form.email.data,
                                     password=form.password.data,
                                     p_phone=form.phone.data,
                                     p_birth_date=form.birthdate.data,
                                     p_sex=form.sex.data
                                     )
        db.session.add(patient_to_create)
        db.session.commit()
        # Specify the type of the user
        session["role"] = "Patient"
        login_user(patient_to_create)
        flash(f"Account created successfully! You are now logged in as {patient_to_create.p_username}", category='success')
        return redirect(url_for('p_profile'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def login_page():
    session["role"]="Default"
    form = LoginForm()
    if form.validate_on_submit():
        if form.role.data == "Admin":
            # Specify the type of the user
            session["role"] = form.role.data
            attempted_admin = Admins.query.filter_by(a_username=form.username.data).first()
            if attempted_admin and attempted_admin.check_password_correction(
                    attempted_password=form.password.data
            ):
                login_user(attempted_admin)
                flash(f'Success! You are logged in as: {attempted_admin.a_username}', category='success')
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Username and password are not match! Please try again', category='danger')
        elif form.role.data == "Doctor":
            # Specify the type of the user

            session["role"] = form.role.data
            attempted_doctor = Doctors.query.filter_by(d_username=form.username.data).first()
            if attempted_doctor and attempted_doctor.check_password_correction(
                    attempted_password=form.password.data
            ):
                login_user(attempted_doctor)
                flash(f'Success! You are logged in as: {attempted_doctor.d_username}', category='success')
                return redirect(url_for('doc_profile'))
            else:
                flash('Username and password are not match! Please try again', category='danger')
        else:
            # Specify the type of the user
            session["role"] = form.role.data
            attempted_patient = Patients.query.filter_by(p_username=form.username.data).first()
            if attempted_patient and attempted_patient.check_password_correction(
                    attempted_password=form.password.data
            ):
                login_user(attempted_patient)
                flash(f'Success! You are logged in as: {attempted_patient.p_username}', category='success')

                return redirect(url_for('p_profile'))
            else:
                flash('Username and password are not match! Please try again', category='danger')
    return render_template('signin.html', form=form)


@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    session.clear()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))



@app.route('/sendmail', methods=['GET', 'POST'])
def send_msg():
    if request.method == 'POST':
        msg = request.form['msg']
        subject = request.form['subject']
        our_mail = "team3@gmail.com"
        return redirect(f'https://mail.google.com/mail/?view=cm&fs=1&to={our_mail}&su={subject}&body={msg}&')

    
