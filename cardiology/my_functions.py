import datetime
from cardiology.models import Appointments, Doctors, Patients, examin
import os
import secrets
import re


def parse_time(day, time):
    d = day.split('-')
    t = time.split(':')
    x = datetime.date(int(d[0]), int(d[1]), int(d[2]))
    y = datetime.time(int(t[0]), int(t[1]))
    return x, y


def generate_gcalendar_link(title: str, description: str, start: datetime, end: datetime):
    return f'https://www.google.com/calendar/render?action=TEMPLATE&text={title}&details={description}&dates={re.sub("[-:]", "", start.isoformat()).split(".", 1)[0]}/{re.sub("[-:]", "", end.isoformat()).split(".", 1)[0]}'


def availabe_appointments(doc, day):
    all_appointmnts = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30']
    reserved_appointments = Appointments.query.filter_by(d_id=doc.d_id, date=day).all()
    reserved_times = [i.Time.strftime('%H:%M') for i in reserved_appointments]
    availabe_time = list(set(all_appointmnts) - set(reserved_times))

    return sorted(availabe_time)





def any_name(list, type):
    names=[0]
    if type=='patient':
        for p in list:
            names.append(Patients.query.filter_by(p_id=p.p_id).first())
        return names
    else:
        for d in list:
            names.append(Doctors.query.filter_by(d_id=d.d_id).first())
        return names



    


def save_picture(form_picture, folder_name):
    fname = secrets.token_hex(16)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = fname + f_ext
    basepath = os.path.dirname(__file__)
    picture_path = os.path.join(f'{basepath}/static/{folder_name}', picture_fn)
    form_picture.save(picture_path)
    saving_path = f'../static/{folder_name}/{picture_fn}'
    return saving_path

def sorting_appointments(appointments, type):
    appoints = [x for x in appointments if x.date>=datetime.date.today()]
    appoints = sorted(appoints, key= lambda x:parse_time2(x.date,x.Time))

    if type=='patient':
        if len(appoints)>=3:
            return appoints[0:3]
        else:
            return appoints[0:len(appoints)]
    return appoints


def doct_patient(examin_list):
    patients=[]
    for i in examin_list:
        p= Patients.query.filter_by(p_id=i.p_id).first()
        patients.append(p)
    patients = list(set(patients))
    return patients




def parse_time2(day, time):
    d = str(day).split('-')
    t = str(time).split(':')
    x = datetime.datetime(int(d[0]), int(d[1]), int(d[2]),int(t[0]), int(t[1]))
    y = datetime.time(int(t[0]), int(t[1]))
    return x    

def count_patients(doctors):
    num=[0]
    for doc in doctors :
        a = Appointments.query.filter_by(d_id=doc.d_id).all()
        p = doct_patient(a)
        num.append(len(p))
    return num

def sorting_docs(doctors):
    docs=sorted(doctors, key= lambda x:len(examin.query.filter_by(d_id=x.d_id).all()), reverse=True)
    return docs

