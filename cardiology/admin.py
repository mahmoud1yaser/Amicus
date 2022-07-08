from flask import render_template, redirect, url_for, request, flash, session
from cardiology.models import Doctors, Patients, Admins, Appointments, examin
from cardiology import app, db
from cardiology.forms import editDoctorForm_foreign, addDoctorForm, addAdminForm, editAdminForm
from cardiology.my_functions import save_picture, count_patients, doct_patient, sorting_docs
from flask_login import current_user, login_required

docs = Doctors.query.all()
patients = Patients.query.all()
appoints = Appointments.query.all()


@app.route('/AdminDashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    # For the dynamic navbar
    active = 'dashboard'
    session['patient_id'] = 0
    if session["role"] == "Admin":
        if request.method == 'POST':
            session['doc_id'] = request.form['id']

            return redirect(url_for('view_selected_doctor'))
        docs = Doctors.query.all()
        patients = Patients.query.all()
        appoints = Appointments.query.all()
        dnumber = len(docs)
        pnumber = len(patients)
        appoinumber = len(appoints)
        sorted_docs = sorting_docs(docs)
        doctor_pnumber = count_patients(sorted_docs)
        return render_template('admin.html', active=active, current_user=current_user, docs=sorted_docs,
                               dnumber=dnumber, pnumber=pnumber, appoinumber=appoinumber, doctor_pnumber=doctor_pnumber)
    else:
        render_template('page403.html')


@app.route('/updateadminpic', methods=['GET', 'POST'])
@login_required
def update_adminPic():
    if session["role"] == "Admin":
        if request.method == 'POST':
            new_path = save_picture(request.files['myfile'], 'profile_pics')
            current_user.a_photo = new_path
            db.session.commit()
            return redirect(url_for('admin_dashboard'))


@app.route('/AdminPatients', methods=['GET', 'POST'])
@login_required
def view_admin_patients():
    # For the dynamic navbar
    active = 'AdminPatients'
    p = 0
    if session["role"] == "Admin":
        if int(session['patient_id']) != 0:
            p = Patients.query.filter_by(p_id=int(session['patient_id'])).first()

        if request.method == 'POST':
            session['patient_id'] = int(request.form['id'])
            return redirect(url_for('view_admin_patients'))

        return render_template('admin_patient.html', active=active, current_user=current_user, patients=patients, p=p,
                               selected_id=int(session['patient_id']), )
    else:
        render_template('page403.html')


@app.route('/DoctorView')
@login_required
def view_selected_doctor():
    # For the dynamic navbar
    active = 'DoctorView'
    if session["role"] == "Admin":
        doct = Doctors.query.filter_by(d_id=int(session['doc_id'])).first()
        examin_list = examin.query.filter_by(d_id=doct.d_id).all()
        doc_patients = doct_patient(examin_list)
        return render_template('admin_doctor.html', current_user=current_user, doc=doct, doc_patients=doc_patients,
                               active=active)
    else:
        render_template('page403.html')


@app.route('/AddAdmin', methods=['GET', 'POST'])
@login_required
def add_admin():
    # For the dynamic navbar
    active = 'AddAdmin'
    if session["role"] == "Admin":
        form = addAdminForm()
        if form.validate_on_submit():
            admin_to_create = Admins(a_username=form.username.data,
                                     a_name=form.fullname.data,
                                     a_email=form.email.data,
                                     password=form.password.data, )
            db.session.add(admin_to_create)
            db.session.commit()
            flash(f'admin {admin_to_create.a_name} account is added', category='success')
            return redirect(url_for('admin_dashboard'))
        if form.errors != {}:  # If there are not errors from the validations
            for err_msg in form.errors.values():
                flash(f'There was an error with creating a user: {err_msg}', category='danger')

        return render_template('add_admin.html', form=form, current_user=current_user, active=active)
    else:
        render_template('page403.html')


@app.route('/AddDoctor', methods=['GET', 'POST'])
@login_required
def add_doctor():
    # For the dynamic navbar
    active = 'AddDoctor'
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
            flash(f'doctor {current_user.a_name} account is added', category='success')
            return redirect(url_for('admin_dashboard'))
        if form.errors != {}:  # If there are not errors from the validations
            for err_msg in form.errors.values():
                flash(f'There was an error with creating a user: {err_msg}', category='danger')

        return render_template('add_doctor.html', form=form, current_user=current_user, active=active)
    else:
        render_template('page403.html')


@app.route('/EditDoctorInfo', methods=['GET', 'POST'])
@login_required
def edit_doctor():
    # For the dynamic navbar
    active = 'EditDoctorInfo'
    if session["role"] == "Admin":

        doct = Doctors.query.filter_by(d_id=int(session['doc_id'])).first()
        form = editDoctorForm_foreign()
        if form.validate_on_submit():

            updatedDoctor = Doctors.query.get(doct.d_id)
            updatedDoctor.d_email = form.email.data
            updatedDoctor.password = form.password.data
            updatedDoctor.d_position = form.position.data
            updatedDoctor.d_salary = form.salary.data
            updatedDoctor.d_workperiod = str(form.work_periodFrom.data) + " " + str(form.work_periodTo.data)
            db.session.commit()

            flash(f'doctor {updatedDoctor.d_name} account is updated', category='success')
            return redirect(url_for('admin_dashboard'))
        if form.errors != {}:  # If there are not errors from the validations
            for err_msg in form.errors.values():
                flash(f'There was an error with editing the doctor: {err_msg}', category='danger')

        return render_template('edit_doctor_from_admin.html', form=form, current_user=current_user, doc=doct,
                               active=active)
    else:
        render_template('page403.html')


@app.route('/EditAdminInfo', methods=['GET', 'POST'])
@login_required
def edit_admin():
    # For the dynamic navbar
    active = 'EditAdminInfo'
    # Setting the logged in user type
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
        return render_template('edit_admin.html', form=form, current_user=current_user, active=active)
    else:
        render_template('page403.html')
