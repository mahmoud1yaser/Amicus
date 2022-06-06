from flask import render_template, redirect, url_for, request, flash, Markup
from flask_sqlalchemy import SQLAlchemy
from cardiology.models import Doctors, Patients, Admins, Appointments, Medical_records, p_Messages, Scans, Prescription
from cardiology.forms import editPatientForm
from cardiology import app, db, doctor
from datetime import datetime, timedelta
from cardiology.my_functions import parse_time, generate_gcalendar_link, availabe_appointments, save_picture
from flask_login import current_user, login_required
# ---------------------------------
p_user = current_user
doctors = Doctors.query.all()
day = 0
doc = 0



# ---------------------------------


@app.route('/PatientProfile', methods=['GET', 'POST'])
@login_required
def p_profile():
    # p_user.p_photo = save_picture(request.files['photo'], 'profile_pics')
    sidebar_active='p_profile'
    MR = Medical_records.query.filter_by(p_id=p_user.p_id).first()
    PRs = Prescription.query.filter_by(p_id=p_user.p_id).all()
    appoints = Appointments.query.filter_by(p_id=p_user.p_id).all()
    appoints = sorting_appointments(appoints, 'patient')
    PRs.reverse()
    if request.method == 'POST':
        pic_path = scan_path = save_picture(request.files['myfile'], 'profile_pics')
        p_user.p_photo
    return render_template('patient_profile.html', user=p_user, MR=MR, PRs=PRs, appoints=appoints, active=sidebar_active)


@app.route('/BookAppointment', methods=['GET', 'POST'])
@login_required
def book_appointment():
    global doc, day
    sidebar_active='book_appointment'
    if request.method == 'POST':
        doc = Doctors.query.filter_by(d_id=request.form['doctors']).first()
        day = request.form['date']
        
        return redirect(url_for('doc_appointments'))

    return render_template('Booking.html', user=p_user, doctors=doctors, active=sidebar_active)


@app.route('/AvailableAppointment', methods=['GET', 'POST'])
@login_required
def doc_appointments():
    sidebar_active='book_appointment'    
    if request.method == 'POST':
        hour = request.form['Time']
        p_date, p_time = parse_time(day, hour)
        appoint = Appointments(p_id=p_user.p_id, p_name=p_user.p_name,
                               d_name=doc.d_name, d_id=doc.d_id, date=p_date, Time=p_time)
        db.session.add(appoint)
        db.session.commit()
        # google_calendar = generate_gcalendar_link("Appointment with dr {doc.d_name} at cardiology department",
        #                                           "", p_time,
        #                                           timedelta(p_time.split(':')[0], p_time.split(':')[1]) + timedelta(
        #                                               minutes=30))
        # flash(Markup(
            # f'A new appointment is created, <a href="{google_calendar}" target="_blank">save the appointment to your calendar</a>'),
            #   'success')
        return redirect(url_for('book_appointment'))

    available_time = availabe_appointments(doc, day)
    return render_template('book2.html', user=p_user, time=available_time, active=sidebar_active)


@app.route('/contact', methods=['POST', 'GET'])
@login_required
def contact_page():
    sidebar_active='contact_page'
    if request.method == 'POST':
        _text = request.form['Message']
        doc = Doctors.query.filter_by(d_id=request.form['doctor']).first()
        message1 = p_Messages(p_id=p_user.p_id, p_name=p_user.p_name, d_id=doc.d_id,
                              d_name=doc.d_name, message=_text, msg_date=datetime.now())
        db.session.add(message1)
        db.session.commit()
        # flash('Message is sent successfully')

    return render_template('contact.html', user=p_user, doctors=doctors, active=sidebar_active)


@app.route('/scans', methods=['POST', 'GET'])
@login_required
def scans_page():
    sidebar_active='scans_page'
    i = 1
    if request.method == 'POST':
        scan_path = save_picture(request.files['myfile'], 'scans')
        scan = Scans(p_id=p_user.p_id, p_name=p_user.p_name, scan_path=scan_path, scan_date=datetime.now())
        db.session.add(scan)
        db.session.commit()
        # flash('Your scan is uploaded')

    patient_scans = Scans.query.filter_by(p_id=p_user.p_id).all()
    return render_template('scans.html', user=p_user, scans=patient_scans, i=i, active=sidebar_active)


# needs validation
@app.route('/EditPatientProfile', methods=['POST', 'GET'])
@login_required
def edit_patient():
    form = editPatientForm()
    if form.validate_on_submit():
        current_user.p_email = form.email.data
        current_user.password = form.password.data
        current_user.p_username = form.username.data
        current_user.p_phone = form.phone.data
        db.session.commit()
        flash(f'patient {current_user.p_name} account is updated', category='success')
        return redirect(url_for('p_profile'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with editing the admin: {err_msg}', category='danger')
    return render_template('edit_patient.html', user=current_user, form=form)