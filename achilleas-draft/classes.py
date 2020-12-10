import datetime
import pickle

try:
    pickle_patients = open("pickles/db_patients.pickle", "rb")

    pickle_doctors = open("pickles/db_doctors.pickle", "rb")

    pickle_admins = open("pickles/db_admins.pickle", "rb")

except (FileNotFoundError, OSError, IOError):
    DB_Patients = {}
    DB_Doctors = {}
    DB_Admins = {}


CALENDAR_ENTRY_TYPES = tuple("BLOCK")


class Appointment:
    def __init__(self, date_time: datetime, doctor_email: str, reason: str = None):
        self.datetime = date_time
        self.doctor_email = doctor_email
        self.reason = reason
        self.prescriptions = []
        self.description = []

    def add_prescription(self, prescription: str):
        self.prescriptions.append(prescription)

    def add_note(self, note: str):
        self.description.append(note)

    def __str__(self):
        gp = DB_Doctors[self.doctor_email]

        notes = ""
        for note in self.description:
            notes = notes + ", " + note

        prescriptions = ""
        for prescription in self.prescriptions:
            prescriptions = prescriptions + ", " + prescription

        print_result = f"{self.datetime} | GP: Dr. {gp.l_name} \n" \
                       f"Prescriptions: {prescriptions} \n" \
                       f"Notes: {notes}"

        return print_result


class Calendar:
    def __init__(self):
        self.schedule = {}

    def get_schedule(self):
        dates_descending = list(self.schedule.keys())
        dates_descending.sort(reverse=True)

        for element in dates_descending:
            entry = self.schedule[element]
            print(str(element) + " |" + entry["type"] + ": " + entry['title'])

    def add_entry(self, date_time: datetime, entry_title: str, patient_email: str = None, entry_type: str = None):
        self.schedule[date_time] = {"title": entry_title, "patient": patient_email, "type": entry_type}

    def update_entry(self, date_time: datetime, entry_title: str, patient_email: str = None, entry_type: str = None):
        self.schedule[date_time] = {"title": entry_title, "patient": patient_email, "type": entry_type}

    def remove_entry(self, date_time: datetime):
        del self.schedule[date_time]


class User:
    def __init__(self, email: str, f_name: str, l_name: str, password: str):
        self._email = email
        self.f_name = f_name
        self.l_name = l_name
        self.__password = password

    def get_email(self):
        return self._email

    def set_email(self, new_email: str):
        self._email = new_email

    def get_password(self):
        return self.__password

    def set_password(self, new_password: str):
        self.__password = new_password


class Admin(User):
    def __init__(self, email: str, f_name: str, l_name: str, password: str):
        super(Admin, self).__init__(email, f_name, l_name, password)
        self.notifications = []

    def confirm_all_patient_registrations(self):
        # notifications include patients' emails that need to be confirmed
        confirmed_emails = []
        for email in self.notifications:
            patient = DB_Patients[email]
            patient.confirmed = True
            confirmed_emails.append(email)

        for admin_email in DB_Admins:
            admin = DB_Admins[admin_email]
            # remove confirmed emails (patient accounts) from admin notifications
            admin.notifications = [p_email for p_email in admin.notifications if p_email not in confirmed_emails]

    @staticmethod
    def confirm_patient_registration(email: str):
        # notifications include patients' emails that need to be confirmed
        patient = DB_Patients[email]
        patient.confirmed = True

        for admin_email in DB_Admins:
            admin = DB_Admins[admin_email]
            admin.notifications.remove(email)

    @staticmethod
    def add_gp(email: str, f_name: str, l_name: str, password: str):
        new_gp = GP(email, f_name, l_name, password)
        DB_Doctors[email] = new_gp

    @staticmethod
    def remove_gp(email: str):
        del DB_Doctors[email]

    @staticmethod
    def deactivate_gp(email: str):
        gp = DB_Doctors[email]
        gp.status = False

    @staticmethod
    def reactivate_gp(email: str):
        gp = DB_Doctors[email]
        gp.status = True


class Patient(User):
    def __init__(self, email: str, f_name: str, l_name: str, password: str):
        super(Patient, self).__init__(email, f_name, l_name, password)
        self.role = "Patient"
        self.confirmed = False
        self.appointments = {}
        self.notifications = []

    def get_upcoming_appointments(self):
        dates_descending = list(self.appointments.keys())
        dates_descending.sort(reverse=True)

        for element in dates_descending:
            entry = self.appointments[element]
            gp = DB_Doctors[entry.doctoremail]

            print(element + " | Appointment with: Dr. " + gp.l_name)

    def get_all_appointments(self):
        pass

    def get_appointments_by_date(self, date_time: datetime):
        pass

    def get_appointments_by_gp(self, gp_email: str):
        pass

    def request_appointment(self, date_time: datetime, doctor_email: str, reason: str = None):
        new_appointment = Appointment(date_time, doctor_email, reason)
        self.appointments[date_time] = new_appointment

        gp = DB_Doctors[doctor_email]
        gp.appointments[date_time] = self.get_email()


class GP(User):
    def __init__(self, email: str, f_name: str, l_name: str, password: str):
        super(GP, self).__init__(email, f_name, l_name, password)
        self.role = "GP"
        self.status = True
        self.appointments = {}
        self.notifications = []
        self.calendar = Calendar()

    def block_calendar(self, date_time: datetime, entry_title: str):
        self.calendar.add_entry(date_time=date_time, entry_title=entry_title, entry_type=CALENDAR_ENTRY_TYPES[0])

    def delete_calendar_entry(self, date_time: datetime):
        self.calendar.remove_entry(date_time=date_time)

    def cancel_appointment(self, date_time: datetime):
        patient_email = self.appointments[date_time]
        patient = DB_Patients[patient_email]

        del patient.appointments[date_time]
        del self.appointments[date_time]

    @staticmethod
    def prescribe(patient_email: str, appointment_datetime: datetime, prescription: str):

        patient = DB_Patients[patient_email]

        appointment = patient.appointments[appointment_datetime]
        appointment.add_prescription(prescription)

    @staticmethod
    def add_appointment_notes(patient_email: str, appointment_datetime: datetime, note: str):
        patient = DB_Patients[patient_email]

        appointment = patient.appointments[appointment_datetime]
        appointment.add_note(note)


# close pickle files
DB_Patients = pickle.load(pickle_patients)
pickle_patients.close()

DB_Doctors = pickle.load(pickle_doctors)
pickle_doctors.close()

DB_Admins = pickle.load(pickle_admins)
pickle_admins.close()
