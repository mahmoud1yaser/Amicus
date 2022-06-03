import datetime
from cardiology.models import Appointments
import os
import secrets

def parse_time(day, time):
    
    d = day.split('-')
    t= time.split('-')
    x = datetime.date(int(d[0]), int(d[1]), int(d[2]))
    y = datetime.time(int(t[0]), int(t[1]))
    return x, y




def generate_gcalendar_link(title: str, description: str, start: datetime, end: datetime):

    return f'https://www.google.com/calendar/render?action=TEMPLATE&text={title}&details={description}&dates={re.sub("[-:]", "", start.isoformat()).split(".", 1)[0]}/{re.sub("[-:]", "", end.isoformat()).split(".", 1)[0]}'





def availabe_appointments(doc, day):
    all_appointmnts = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30']
    reserved_appointments = Appointments.query.filter_by(d_id=doc.d_id, date=day).all()
    reserved_times = [i.Time.strftime('%H:%M') for i in reserved_appointments]
    availabe_time = list(set(all_appointmnts)-set(reserved_times))

    return availabe_time





def save_picture(form_picture, folder_name):
    fname = secrets.token_hex(16)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = fname + f_ext
    basepath = os.path.dirname(__file__)
    picture_path = os.path.join(basepath, f'cardiology/static/{folder_name}', picture_fn)
    form_picture.save(picture_path)
    return picture_path



