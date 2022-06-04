from crypt import methods
from flask import render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from cardiology.models import Doctors, Patients, Admins, Appointments, Medical_records, p_Messages, Scans, Prescription
from cardiology import app, db, patient
from datetime import datetime
from my_functions import parse_time, save_picture
#
#
# a_user = Admins.query.filter_by(a_id=1)
# docs = Doctors.query.all()
# patients = Patients.query.all()
#
# @app.route('/AdminDashboard')
# def admin_dashboard():
#
#     return render_template('.html', user=a_user, docs=docs)
#
#
#
# @app.route('/DepartmentPatients')
# def dep_patients():
#     return render_template('.html', patients=patients, user=a_user)
#
# # needs validation
# @app.route('/AddDoctor', methods=['GET', 'POST'])
# def add_doctors():
#
#     if request.method == 'POST':
#         bd, nothing= parse_time(request.form['birthdate'],'10-10')
#
#         new_doc = Doctors(d_username=request.form['username'], d_password=request.form['password'],
#         d_name=request.form['name'], d_email=request.form['email'], d_phone=request.form['phone'],
#         d_birth_date=bd, d_sex=request.form['sex'], d_salary =float(request.form['salary']),
#         d_position= request.form['position'] )
#
#         db.session.add(new_doc)
#         db.session.commit()
#         flash(f'doctor {new_doc.d_name} account is created')
#
#     return render_template('.html', user=a_user)
#
#
# # needs validation
# @app.route('/EditDoctorInfo', methods=['GET', 'POST'])
# def edit_doc():
#
#     if request.method == 'POST':
#         edited_doc = Doctors.query.filter_by(d_id=request.form['id'])
#         edited_doc.d_username = request.form['username']
#         edited_doc.d_password = request.form['passward']
#         edited_doc.d_email = request.form['email']
#         edited_doc.d_phone = request.form['phone']
#         edited_doc.d_salary = request.form['salary']
#         edited_doc.d_position = request.form['position']
#
#         flash(f'doctor {edited_doc.u_name} account is updated')
#
#     return render_template('.html', user=a_user,)
#
#
#
#
#
#
#