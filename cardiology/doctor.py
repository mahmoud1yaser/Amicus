from cardiology.forms import editDoctorForm_primary
from flask import render_template, redirect, url_for, request, flash, session
from cardiology.models import Patients, Appointments, Medical_records, p_Messages, Scans, Prescription, \
    examin
from cardiology import app, db
from datetime import date
from cardiology.my_functions import save_picture, sorting_appointments, any_name
from flask_login import current_user, login_required




@app.route('/DoctorProfile', methods=['GET', 'POST'])
@login_required
def doc_profile():
    if session["role"] == "Doctor":
        active = 'profile'
        doc_patients = examin.query.filter_by(d_id=current_user.d_id).all()
        p_names1 = any_name(doc_patients, 'patient')

        doc_msgs = p_Messages.query.filter_by(d_id=current_user.d_id).all()
        p_names2 = any_name(doc_msgs, 'patient')

        if request.method == 'POST':

            try:
                session['patient_id'] = int(request.form['p_id'])
                a = Patients.query.filter_by(p_id=session['patient_id']).all()
                if a == []:
                    flash('Please enter correct id.')
            except:
                flash('Please enter correct id.')
            return redirect(url_for('patient_info'))
        return render_template('Doctor.html', user=current_user, pats=doc_patients, msgs=doc_msgs, active=active,
                               p_names=p_names1, p_names2=p_names2)
    else:
        render_template('page403.html')


@app.route('/updatepic', methods=['GET', 'POST'])
@login_required
def update_docPic():
    if session["role"] == "Doctor":
        if request.method == 'POST':
            new_path = save_picture(request.files['myfile'], 'profile_pics')
            current_user.d_photo = new_path
            db.session.commit()
            return redirect(url_for('doc_profile'))


@app.route("/viewmore", methods=['GET', 'POST'])
@login_required
def view_more():
    if session["role"] == "Doctor":
        active = ' '
        global selected_patient
        if request.method == 'POST':
            session['patient_id'] = int(request.form['gg'])
            return redirect(url_for('patient_info'))
    else:
        render_template('page403.html')


@app.route('/PatientInfo')
@login_required
def patient_info():
    if session["role"] == "Doctor":
        active = 'profile'
        MR = Medical_records.query.filter_by(p_id=Patients.query.filter_by(
            p_id=int(session['patient_id'])).first().p_id).first()
        PRs = Prescription.query.filter_by(p_id=Patients.query.filter_by(
            p_id=int(session['patient_id'])).first().p_id).all()
        appoints = Appointments.query.filter_by(p_id=Patients.query.filter_by(
            p_id=int(session['patient_id'])).first().p_id).all()
        appoints = sorting_appointments(appoints, 'patient')
        PRs.reverse()
        d_obj = any_name(PRs, 'doctor')
        return render_template('Doctor_Patients.html', user=current_user, patient=Patients.query.filter_by(
            p_id=int(session['patient_id'])).first(), MR=MR, PRs=PRs,
                               appoints=appoints, active=active, d_obj=d_obj)
    else:
        render_template('page403.html')


@app.route('/AddMedicalRecord', methods=['GET', 'POST'])
@login_required
def add_MR():
    if session["role"] == "Doctor":
        active = 'profile'
        if request.method == 'POST':
            if Medical_records.query.filter_by(p_id=int(session['patient_id'])).all() == []:
                new_MR = Medical_records(p_id=int(session['patient_id']), d_id=current_user.d_id,
                                         diseases_history=request.form['medical_history'],
                                         restricted_drugs=request.form['restricted_drugs'])

                db.session.add(new_MR)
            else:
                mr = Medical_records.query.filter_by(
                    p_id=Patients.query.filter_by(p_id=int(session['patient_id'])).first())
                mr.restricted_drugs = request.form['restricted_drugs']
                mr.diseases_history = request.form['medical_history']
            db.session.commit()
            flash('Medical Record is edited successfully.')
            redirect(url_for('patient_info'))

        return render_template('Write_MD.html', user=current_user, active=active)
    else:
        render_template('page403.html')


@app.route('/AddPrescription', methods=['GET', 'POST'])
@login_required
def add_PR():
    if session["role"] == "Doctor":
        active = 'profile'
        if request.method == 'POST':
            new_PR = Prescription(p_id=int(session['patient_id']), d_id=current_user.d_id,
                                  diagnosis=request.form['diagnosis'],
                                  drugs=request.form['drugs'], pres_date=date.today())

            db.session.add(new_PR)
            db.session.commit()
            flash('Prescription is added successfully.')
            return redirect(url_for('patient_info'))

        return render_template('Add_prescription.html', user=current_user, active=active)
    else:
        render_template('page403.html')


@app.route('/DoctorAppointments')
@login_required
def doctor_appoints():
    if session["role"] == "Doctor":
        active = 'appointments'
        doct_appoints = Appointments.query.filter_by(d_id=current_user.d_id).all()
        doc_appoints = sorting_appointments(doct_appoints, 'doctor')
        p_obj = any_name(doc_appoints, 'patient')

        return render_template('Doc_Appointments.html', user=current_user, appoints=doc_appoints, active=active,
                               p_obj=p_obj)
    else:
        render_template('page403.html')


@app.route('/EditDoctorInformation', methods=['GET', 'POST'])
@login_required
def edit_doc():
    if session["role"] == "Doctor":
        active = 'edit'
        form = editDoctorForm_primary()
        if form.validate_on_submit():
            current_user.d_email = form.email.data
            current_user.password = form.password.data
            current_user.d_username = form.username.data
            current_user.d_phone = form.phone.data
            db.session.commit()
            flash(f'doctor {current_user.d_name} account is updated')
            return redirect(url_for('doc_profile'))
        if form.errors != {}:  # If there are not errors from the validations
            for err_msg in form.errors.values():
                flash(f'There was an error with editing the doctor: {err_msg}')
        return render_template('Doctor_edit.html', user=current_user, form=form, active=active)
    else:
        render_template('page403.html')


@app.route('/PatientScans')
@login_required
def patient_scans():
    if session["role"] == "Doctor":
        active = 'scans'
        patient_scans = Scans.query.filter_by(p_id=Patients.query.filter_by(
            p_id=int(session['patient_id'])).first().p_id).all()
        return render_template('Patient_Scans.html', user=current_user, scans=patient_scans, active=active)
    else:
        render_template('page403.html')
