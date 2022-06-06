from cardiology.forms import editDoctorForm_primary
from flask import render_template, redirect, url_for, Flask, request, flash, session, Response
from flask_sqlalchemy import SQLAlchemy
from cardiology.models import Doctors, Patients, Admins, Appointments, Medical_records, p_Messages, Scans, Prescription
from cardiology import app, db
from datetime import datetime, date
from cardiology.my_functions import save_picture, doct_patient, sorting_appointments
from flask_login import current_user, login_required

# # -------------------------------------
# current_user = Doctors.query.filter_by(d_id=1).first()
# # selected_patient = Patients.query.filter_by(p_id=3).first()
# selected_patient = 0
# # -------------------------------------
#
# current_user = Doctors.query.filter_by(d_id=1)


@app.route('/DoctorProfile', methods=['GET', 'POST'])
@login_required
def doc_profile():
    if session["role"] == "Doctor":
        
        doc_appoints = Appointments.query.filter_by(d_id=current_user.d_id).all()
        doc_patients = doct_patient(doc_appoints)
        doc_msgs = p_Messages.query.filter_by(d_id=current_user.d_id).all()
        if request.method == 'POST':
            patient_id = request.form['p_id']
            session['selected_patient'] = Patients.query.filter_by(
                p_id=int(patient_id)).first()
            return redirect(url_for('patient_info'))
        return render_template('Doctor.html', user=current_user, patients=doc_patients, msgs=doc_msgs)
    else:
        render_template('page403.html')


@app.route('/updatepic', methods=['GET', 'POST'])
@login_required
def update_docPic():
    if session["role"] == "Doctor":
        if request.method == 'POST':
            new_path= save_picture(request.files['myfile'], 'profile_pics')
            current_user.d_photo = new_path
            db.session.commit()
            return redirect(url_for('doc_profile'))


@app.route("/viewmore", methods=['GET', 'POST'])
@login_required
def view_more():
    if session["role"] == "Doctor":
        global selected_patient
        if request.method == 'POST':
            patient_id = request.form['gg']
            session['selected_patient'] = Patients.query.filter_by(
                p_id=int(patient_id)).first()
            return redirect(url_for('patient_info'))
    else:
        render_template('page403.html')


@app.route('/PatientInfo')
@login_required
def patient_info():
    if session["role"] == "Doctor":
        MR = Medical_records.query.filter_by(p_id=session['selected_patient'].p_id).first()
        PRs = Prescription.query.filter_by(p_id=session['selected_patient'].p_id).all()
        appoints = Appointments.query.filter_by(p_id=session['selected_patient'].p_id).all()
        appoints = sorting_appointments(appoints, 'patient')
        PRs.reverse()
        return render_template('Doctor_Patients.html', user=current_user, patient=session['selected_patient'], MR=MR, PRs=PRs,
                               appoints=appoints)
    else:
        render_template('page403.html')


@app.route('/AddMedicalRecord', methods=['GET', 'POST'])
@login_required
def add_MR():
    if session["role"] == "Doctor":
        if request.method == 'POST':
            if Medical_records.query.filter_by(p_id=session['selected_patient'].p_id).all() == []:
                new_MR = Medical_records(p_id=session['selected_patient'].p_id, p_name=session['selected_patient'].p_name, d_id=current_user.d_id,
                                         d_name=current_user.d_name, diseases_history=request.form['medical_history'],
                                         restricted_drugs=request.form['restricted_drugs'])
                db.session.add(new_MR)
            else:
                mr = Medical_records.query.filter_by(
                    p_id=session['selected_patient'].p_id).first()
                mr.restricted_drugs = request.form['restricted_drugs']
                mr.diseases_history = request.form['medical_history']
            db.session.commit()
            flash('Medical Record is edited successfully.')
            redirect(url_for('patient_info'))

        return render_template('Write_MD.html', user=current_user)
    else:
        render_template('page403.html')


@app.route('/AddPrescription', methods=['GET', 'POST'])
@login_required
def add_PR():
    if session["role"] == "Doctor":
        if request.method == 'POST':
            new_PR = Prescription(p_id=session['selected_patient'].p_id, p_name=session['selected_patient'].p_name, d_id=current_user.d_id,
                                  d_name=current_user.d_name, diagnosis=request.form[
                    'diagnosis'], drugs=request.form['drugs'],
                                  pres_date=date.today())
            db.session.add(new_PR)
            db.session.commit()
            flash('Prescription is added successfully.')
            return redirect(url_for('patient_info'))

        return render_template('Add_prescription.html', user=current_user)
    else:
        render_template('page403.html')


@app.route('/DoctorAppointments')
@login_required
def doctor_appoints():
    if session["role"] == "Doctor":
        doct_appoints = Appointments.query.filter_by(d_id=current_user.d_id).all()
        doc_appoints = sorting_appointments(doct_appoints, 'doctor')

        return render_template('Doc_Appointments.html', user=current_user, appoints=doc_appoints)
    else:
        render_template('page403.html')


@app.route('/EditDoctorInformation', methods=['GET', 'POST'])
@login_required
def edit_doc():
    if session["role"] == "Doctor":
        form = editDoctorForm_primary()
        if form.validate_on_submit():
            current_user.d_email = form.email.data
            current_user.password = form.password.data
            current_user.d_username = form.username.data
            current_user.d_phone = form.phone.data
            db.session.commit()
            print(f'doctor {current_user.d_name} account is updated')
            return redirect(url_for('doc_profile'))
        if form.errors != {}:  # If there are not errors from the validations
            for err_msg in form.errors.values():
                print(f'There was an error with editing the doctor: {err_msg}')
        return render_template('Doctor_edit.html', user=current_user, form=form)
    else:
        render_template('page403.html')


@app.route('/PatientScans')
@login_required
def patient_scans():
    if session["role"] == "Doctor":
        patient_scans = Scans.query.filter_by(p_id=session['selected_patient'].p_id).all()
        return render_template('Patient_Scans.html', user=current_user, scans=patient_scans)
    else:
        render_template('page403.html')

