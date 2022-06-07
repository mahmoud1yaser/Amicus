from flask import render_template, redirect, url_for, request, flash, session, Response
from flask_sqlalchemy import SQLAlchemy
from wtforms import ValidationError
from cardiology.models import Doctors, Patients, Admins, Appointments, Medical_records, p_Messages, Scans, Prescription
from cardiology import app, db
from cardiology.forms import editDoctorForm_foreign, addDoctorForm, addAdminForm, editAdminForm
from datetime import datetime
from cardiology.my_functions import parse_time, save_picture, count_patients, doct_patient, sorting_docs
from flask_login import current_user, login_required

 
docs = Doctors.query.all()
patients = Patients.query.all()
appoints = Appointments.query.all()


@app.route('/AdminDashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    session['patient_id'] = 0
    if session["role"] == "Admin":
        if request.method == 'POST':
            session['doc_id']= request.form['id']
             
            return redirect(url_for('view_selected_doctor'))
        docs = Doctors.query.all()
        patients = Patients.query.all()
        appoints = Appointments.query.all()
        dnumber = len(docs)
        pnumber = len(patients)
        appoinumber = len(appoints)
        sorted_docs= sorting_docs(docs)
        doctor_pnumber = count_patients(sorted_docs)
        return render_template('admin.html', current_user=current_user, docs=sorted_docs, dnumber=dnumber, pnumber=pnumber, appoinumber=appoinumber, doctor_pnumber=doctor_pnumber)
    else:
        render_template('page403.html')


@app.route('/updateadminpic', methods=['GET', 'POST'])
@login_required
def update_adminPic():
    if session["role"] == "Admin":
        if request.method == 'POST':
            new_path= save_picture(request.files['myfile'], 'profile_pics')
            current_user.a_photo = new_path
            db.session.commit()
            return redirect(url_for('admin_dashboard'))

@app.route('/AdminPatients', methods=['GET', 'POST'])
@login_required
def view_admin_patients():
    p = 0
    if session["role"] == "Admin":
        if int(session['patient_id']) != 0:
            p = Patients.query.filter_by(p_id = int(session['patient_id'])).first()
           
        if request.method == 'POST':
            session['patient_id'] = int(request.form['id'])
            return redirect(url_for('view_admin_patients'))
            
    
        return render_template('admin_patient.html', current_user=current_user, patients=patients, p=p, selected_id=int(session['patient_id']), )
    else:
        render_template('page403.html')


@app.route('/DoctorView')
@login_required
def view_selected_doctor():
    if session["role"] == "Admin":
        doct= Doctors.query.filter_by(d_id=int(session['doc_id'])).first()
        appoint = Appointments.query.filter_by(d_id=doct.d_id).all()
        doc_patients = doct_patient(appoint)
        return render_template('admin_doctor.html', current_user=current_user, doc=doct, doc_patients=doc_patients)
    else:
        render_template('page403.html')


@app.route('/AddAdmin', methods=['GET', 'POST'])
@login_required
def add_admin():
    if session["role"] == "Admin":
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
    else:
        render_template('page403.html')


@app.route('/AddDoctor', methods=['GET', 'POST'])
@login_required
def add_doctor():
    if session["role"] == "Admin":
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
            flash(f'admin {current_user.a_name} account is added', category='success')
            return redirect(url_for('admin_dashboard'))
        if form.errors != {}:  # If there are not errors from the validations
            for err_msg in form.errors.values():
                flash(f'There was an error with creating a user: {err_msg}', category='danger')

        return render_template('add_doctor.html', form=form, current_user=current_user)
    else:
        render_template('page403.html')


# needs validation
@app.route('/EditDoctorInfo', methods=['GET', 'POST'])
@login_required
def edit_doctor():
    if session["role"] == "Admin":
        form = editDoctorForm_foreign()
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

        return render_template('edit_doctor_from_admin.html', form=form, current_user=current_user)
    else:
        render_template('page403.html')


@app.route('/EditAdminInfo', methods=['GET', 'POST'])
@login_required
def edit_admin():
    if session["role"] == "Admin":
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
    else:
        render_template('page403.html')
