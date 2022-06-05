from flask import render_template, redirect, url_for, Flask, request, flash
from flask_sqlalchemy import SQLAlchemy
from cardiology.models import Doctors, Patients, Admins, Appointments, Medical_records, p_Messages, Scans, Prescription
from cardiology import app, db
from datetime import datetime
from cardiology.my_functions import parse_time, save_picture

d_user = Doctors.query.filter_by(d_id=1)

@app.route('/DoctorProfile')
def doc_profile():
    
    doc_appoints = Appointments.query.filter_by(d_id=d_user.d_id)
    doc_msgs= p_Messages.query.filter_by(d_id=d_user.d_id)

    return render_template('.html')
