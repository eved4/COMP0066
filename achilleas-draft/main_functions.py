from classes import *


def register_user(email: str, f_name: str, l_name: str, password: str, role: str):
    if role == "patient":
        new_patient = Patient(email, f_name, l_name, password)
        DB_Patients[email] = new_patient

        for admin in DB_Admins:
            this_admin = DB_Admins[admin]
            this_admin.notifications.append(email)
    elif role == "admin":
        new_admin = Admin(email, f_name, l_name, password)
        DB_Admins[email] = new_admin
    else:
        pass


def login(email: str, password: str, role: str):
    email = email.lower()

    if role == "patient":
        if email in DB_Patients:
            user = DB_Patients[email]
            user_password = user.get_password()
            if user_password == password:
                return True
            else:
                return False
        else:
            return False
    elif role == "gp":
        if email in DB_Doctors:
            user = DB_Patients[email]
            user_password = user.get_password()
            if user_password == password:
                return True
            else:
                return False
        else:
            return False
    elif role == "admin":
        if email in DB_Admins:
            user = DB_Patients[email]
            user_password = user.get_password()
            if user_password == password:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def search_appointments_by_datetime(date_time: datetime):
    available_gps = []
    for gp_email in DB_Doctors:
        gp = DB_Doctors[gp_email]
        if date_time not in gp.calendar.schedule:
            available_gps.append(gp)

        if len(available_gps) > 5:
            break

    if not available_gps:
        return None
    else:
        return available_gps


