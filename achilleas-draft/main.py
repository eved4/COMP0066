from main_functions import *
import datetime as dt

# register_user("admin1@gmail.com", "Leo", "Messi", "123", "admin")
# register_user("admin2@gmail.com", "Gerard", "Pique", "123", "admin")
#
# register_user("patient@gmail.com", "Cristiano", "Ronaldo", "123", "patient")
#
# admin1 = DB_Admins["admin1@gmail.com"]
# admin2 = DB_Admins["admin2@gmail.com"]
#
# admin1.add_gp("gp1@gmail.com", "Kylian", "Mbappe", "123")
# admin1.add_gp("gp2@gmail.com", "Antoine", "Griezman", "123")
# admin1.add_gp("gp3@gmail.com", "Paul", "Pogba", "123")

#register_user("patient2@gmail.com", "Sergio", "Ramos", "123", "patient")


user_email = "patient@gmail.com"
user_password = "123"
role = "patient"

login_success = login(user_email, user_password, role)

active_user = None
if login_success:
    if role == "patient":
        active_user = DB_Patients[user_email]

    elif role == "gp":
        active_user = DB_Doctors[user_email]

    elif role == "admin":
        active_user = DB_Admins[user_email]

    else:
        pass


print(login_success)
print(DB_Patients)
print(active_user.f_name, active_user.l_name)


date_time = dt.datetime(2019, 11, 4, 0, 5, 23)
gp = DB_Doctors["gp3@gmail.com"]
gp.block_calendar(date_time, "Pick up kids")

available = search_appointments_by_datetime(date_time)

print(available[0].l_name)
print(available[1].l_name)

patient = DB_Patients["patient@gmail.com"]
patient.request_appointment(date_time, "gp2@gmail.com")

print(patient.appointments)

griezman = DB_Doctors["gp2@gmail.com"]
print(griezman.appointments)

griezman.prescribe("patient@gmail.com", date_time, "Take his drug")
griezman.prescribe("patient@gmail.com", date_time, "Also take his drug")

griezman.add_appointment_notes("patient@gmail.com", date_time, "He has a precondition")


current = patient.appointments[date_time]
print(current.prescriptions)
print(current.description)

#griezman.cancel_appointment(date_time)

#print(griezman.appointments)
#print(patient.appointments)

print(DB_Patients)
print(DB_Doctors)
print(DB_Admins)


pickle_patients = open("pickles/db_patients.pickle", "wb")
pickle.dump(DB_Patients, pickle_patients)
pickle_patients.close()

pickle_doctors = open("pickles/db_doctors.pickle", "wb")
pickle.dump(DB_Doctors, pickle_doctors)
pickle_doctors.close()

pickle_admins = open("pickles/db_admins.pickle", "wb")
pickle.dump(DB_Admins, pickle_admins)
pickle_admins.close()
