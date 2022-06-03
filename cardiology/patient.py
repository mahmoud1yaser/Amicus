from flask import render_template, redirect, url_for, request, flash, Markup
from flask_sqlalchemy import SQLAlchemy
from cardiology.models import Doctors, Patients, Admins, Appointments, Medical_records, p_Messages, Scans, Prescription
from cardiology import app, db, doctor
from datetime import datetime, timedelta, now
from my_functions import parse_time, generate_gcalendar_link, availabe_appointments, save_picture


# ---------------------------------
p_user = Patients.query.filter_by(p_id=1).first()
doctors = Doctors.query.all()
day = 0
doc = 0
medicl_record = 0
# ---------------------------------


@app.route('/PatientProfile')
def p_profile():
    MR = Medical_records.query.filter_by(p_id=p_user.p_id).first()
    PRs = Medical_records.query.filter_by(p_id=p_user.p_id).all()
    PRs.reverse()
    return render_template('.html', user=p_user, medicl_record=MR, perscriptions=PRs)



@app.route('/BookAppointment', methods=['GET', 'POST'])
def book_appointment():
    global doc, day

    if request.method == 'POST':
        doc = Doctors.query.filter_by(d_id=request.form['doctors']).first()
        day = request.form['day']
        redirect(url_for('doc_appointments'))

    return render_template('.html', user=p_user, doctors=doctors)



@app.route('/AvailableAppointment', methods=['GET', 'POST'])
def doc_appointments():

    if request.method == 'POST':

        hour = request.form['Time']
        p_date, p_time = parse_time(day, hour)
        appoint = Appointments(p_id=p_user.p_id, p_name=p_user.p_name,
                               d_name=doc.d_name, d_id=doc.d_id, date=p_date, Time=p_time)
        db.session.add(appoint)
        db.session.commit()
        google_calendar = generate_gcalendar_link("Appointment with dr {doc.d_name} at cardiology department",
                                                  "", p_time, p_time+timedelta(minutes=30))
        flash(Markup(f'A new appointment is created, <a href="{google_calendar}" target="_blank">save the appointment to your calendar</a>'),
              'success')
        redirect(url_for('book_appointment'))

    available_time = availabe_appointments(doc, day)
    return render_template('.html', user=p_user, time=available_time)



@app.route('/contact', methods=['POST', 'GET'])
def contact_page():

    if request.method == 'POST':
        _text = request.form['Message']
        doc = Doctors.query.filter_by(d_id=request.form['doctors']).first()
        message1 = p_Messages(p_id=p_user.p_id, p_name=p_user.p_name, d_id=doc.d_id,
         d_name=doc.d_name, message=_text, msg_date=datetime.now())
        db.session.add(message1)
        db.session.commit()
        flash('Message is sent successfully')

    
    return render_template('.html', user=p_user, doctors=doctors)



@app.route('/scans')
def scans_page():

    if request.method == 'POST':
        scan_path = save_picture(request.files['scan'], 'scans')
        scan = Scans(p_id=p_user.p_id, p_name=p_user.P_name, scan_path=scan_path, scan_date=datetime.now())
        db.session.add(scan)
        db.session.commit()
        flash('Your scan is uploaded')

    patient_scans = Scans.query.filter_by(p_id=p_user.p_id).all
    return render_template('.html', user=p_user, scans=patient_scans)


# needs validation
@app.route('/EditPatientProfile', methods=['POST', 'GET'])
def edit_patient():

    if request.method == 'POST':

        p_user.p_username = request.form['username']
        p_user.p_passward = request.form['passward']
        p_user.p_email = request.form['email']
        p_user.p_phone = request.form['passward']
        p_user.p_photo = save_picture(request.files['photo'], 'profile_pics')
        flash('profile is updated successfully')

    return render_template('.html', user=p_user)
         