from flask import render_template, redirect, url_for, request, flash, Markup, session
from wtforms.validators import ValidationError
from cardiology.models import Doctors, Patients, Appointments, Medical_records, p_Messages, Scans, Prescription, \
    examin
from cardiology.forms import editPatientForm
from cardiology import app, db
from datetime import datetime, timedelta
from cardiology.my_functions import any_name, parse_time, generate_gcalendar_link, availabe_appointments, save_picture, \
    sorting_appointments, parse_time2
from flask_login import current_user, login_required

# ---------------------------------
p_user = current_user
doctors = Doctors.query.all()


# ---------------------------------


@app.route('/PatientProfile', methods=['GET', 'POST'])
@login_required
def p_profile():
    # For the dynamic navbar
    if session["role"] == "Patient":
        # For the dynamic navbar
        sidebar_active = 'p_profile'
        MR = Medical_records.query.filter_by(p_id=current_user.p_id).first()
        PRs = Prescription.query.filter_by(p_id=current_user.p_id).all()
        appoints = Appointments.query.filter_by(p_id=current_user.p_id).all()
        appoints = sorting_appointments(appoints, 'patient')
        PRs.reverse()
        d_obj = any_name(PRs, 'doctor')
        if request.method == 'POST':
            pic_path = save_picture(request.files['myfile'], 'profile_pics')
            current_user.p_photo = pic_path
            db.session.commit()
            return redirect(url_for('p_profile'))
        return render_template('patient_profile.html', user=current_user, MR=MR, PRs=PRs, appoints=appoints,
                               active=sidebar_active, d_obj=d_obj)
    else:
        render_template('page403.html')


@app.route('/BookAppointment', methods=['GET', 'POST'])
@login_required
def book_appointment():
    # Setting the logged in user type
    if session["role"] == "Patient":
        global day
        # For the dynamic navbar
        sidebar_active = 'book_appointment'
        doctors = Doctors.query.all()
        if request.method == 'POST':
            session['doc_id'] = request.form['doctors']
            session['day'] = request.form['date']

            return redirect(url_for('doc_appointments'))

        return render_template('Booking.html', user=current_user, doctors=doctors, active=sidebar_active)
    else:
        render_template('page403.html')


@app.route('/AvailableAppointment', methods=['GET', 'POST'])
@login_required
def doc_appointments():
    # Setting the logged in user type
    if session["role"] == "Patient":
        # For the dynamic navbar
        sidebar_active = 'book_appointment'
        doc = Doctors.query.filter_by(d_id=session['doc_id']).first()
        if request.method == 'POST':
            hour = request.form['Time']
            p_date, p_time = parse_time(session['day'], hour)
            appoint = Appointments(p_id=current_user.p_id,
                                   d_id=doc.d_id, date=p_date, Time=p_time)
            db.session.add(appoint)
            db.session.commit()
            google_calendar = generate_gcalendar_link(
                f"Appointment with dr {Doctors.query.filter_by(d_id=session['doc_id']).first().d_name} at cardiology department",
                "", parse_time2(session['day'], hour),
                parse_time2(session['day'], hour) + timedelta(minutes=30))
            flash(Markup(
                f'A new appointment is created, <a href="{google_calendar}" target="_blank">save the appointment to your calendar</a>'),
                'success')

            if examin.query.filter_by(d_id=doc.d_id, p_id=current_user.p_id).all() == []:
                pat = examin(d_id=doc.d_id, p_id=current_user.p_id)
                db.session.add(pat)
                db.session.commit()
            return redirect(url_for('book_appointment'))

        available_time = availabe_appointments(doc, session['day'])
        return render_template('book2.html', user=current_user, time=available_time, active=sidebar_active)
    else:
        render_template('page403.html')


@app.route('/contact', methods=['POST', 'GET'])
@login_required
def contact_page():
    # Setting the logged in user type
    if session["role"] == "Patient":
        # For the dynamic navbar
        sidebar_active = 'contact_page'
        doctors = Doctors.query.all()
        if request.method == 'POST':
            _text = request.form['Message']
            session['doc_id'] = request.form['doctor']
            message1 = p_Messages(p_id=p_user.p_id, d_id=Doctors.query.filter_by(d_id=session['doc_id']).first().d_id,
                                  message=_text, msg_date=datetime.now())
            db.session.add(message1)
            db.session.commit()
            flash('Message is sent successfully')
    else:
        render_template('page403.html')

    return render_template('contact.html', user=p_user, doctors=doctors, active=sidebar_active)


@app.route('/scans', methods=['POST', 'GET'])
@login_required
def scans_page():
    # Setting the logged in user type
    if session["role"] == "Patient":
        # For the dynamic navbar
        sidebar_active = 'scans_page'
        i = 1
        if request.method == 'POST':
            scan_path = save_picture(request.files['myfile'], 'scans')
            scan = Scans(p_id=p_user.p_id, scan_path=scan_path, scan_date=datetime.now())
            db.session.add(scan)
            db.session.commit()
            flash('Your scan is uploaded')

        patient_scans = Scans.query.filter_by(p_id=p_user.p_id).all()
        return render_template('scans.html', user=p_user, scans=patient_scans, i=i, active=sidebar_active)
    else:
        render_template('page403.html')


@app.route('/EditPatientProfile', methods=['POST', 'GET'])
@login_required
def edit_patient():
    # Setting the logged in user type
    if session["role"] == "Patient":
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
    else:
        render_template('page403.html')
