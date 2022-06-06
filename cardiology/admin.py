from flask import render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import ValidationError
from cardiology.models import Doctors, Patients, Admins, Appointments, Medical_records, p_Messages, Scans, Prescription
from cardiology import app, db, patient
from cardiology.forms import editDoctorForm, addDoctorForm, addAdminForm, editAdminForm
from datetime import datetime
from cardiology.my_functions import parse_time, save_picture
from flask_login import current_user, login_required


a_user = Admins.query.filter_by(a_id=1)
docs = Doctors.query.all()
patients = Patients.query.all()


@app.route('/AdminDashboard')
@login_required
def admin_dashboard():
    return render_template('admin.html', current_user=current_user)


@app.route('/DoctorPatients')
@login_required
def view_doctor_patients():
    return render_template('admin_patient.html', current_user=current_user)


@app.route('/DoctorView')
@login_required
def view_selected_doctor():
    return render_template('admin_doctor.html', current_user=current_user)


@app.route('/AddAdmin', methods=['GET', 'POST'])
@login_required
def add_admin():
    form = addAdminForm()
    if form.validate_on_submit():
        admin_to_create = Admins(a_username=form.username.data,
                                 a_name=form.fullname.data,
                                 a_email=form.email.data,
                                 password=form.password.data, )
        db.session.add(admin_to_create)
        db.session.commit()
        flash(f'doctor {admin_to_create.a_name} account is added', category='success')
        return redirect(url_for('admin_dashboard'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('add_admin.html', form=form, current_user=current_user)


@app.route('/AddDoctor', methods=['GET', 'POST'])
@login_required
def add_doctor():
    form = addDoctorForm()
    if form.validate_on_submit():
        doctor_to_create = Doctors(d_username=form.username.data,
                                   d_name=form.fullname.data,
                                   d_email=form.email.data,
                                   password=form.password.data,
                                   d_phone=form.phone.data,
                                   d_birth_date=form.birthdate.data,
                                   d_sex=form.sex.data,
                                   d_salary=form.salary.data,
                                   d_position=form.position.data,
                                   d_workperiod=str(form.work_periodFrom.data) + " " + str(form.work_periodTo.data))
        db.session.add(doctor_to_create)
        db.session.commit()
        flash(f'doctor {current_user.d_name} account is added', category='success')
        return redirect(url_for('admin_dashboard'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('add_doctor.html', form=form, current_user=current_user)


# needs validation
@app.route('/EditDoctorInfo', methods=['GET', 'POST'])
@login_required
def edit_doctor():
    form = editDoctorForm()
    if form.validate_on_submit():
        current_user.d_email = form.email.data
        current_user.password = form.password.data
        current_user.d_position = form.position.data
        current_user.d_salary = form.salary.data
        current_user.d_workperiod = str(form.work_periodFrom.data) + " " + str(form.work_periodTo.data)
        db.session.commit()
        flash(f'doctor {current_user.d_name} account is updated', category='success')
        return redirect(url_for('admin_dashboard'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with editing the doctor: {err_msg}', category='danger')

    return render_template('admin_doctor.html', form=form, current_user=current_user)


@app.route('/EditAdminInfo', methods=['GET', 'POST'])
@login_required
def edit_admin():
    form = editAdminForm()
    if form.validate_on_submit():
        current_user.a_email = form.email.data
        current_user.password = form.password.data
        current_user.a_name = form.fullname.data
        db.session.commit()
        flash(f'admin {current_user.a_name} account is updated', category='success')
        return redirect(url_for('admin_dashboard'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with editing the admin: {err_msg}', category='danger')
    return render_template('edit_admin.html', form=form, current_user=current_user)
