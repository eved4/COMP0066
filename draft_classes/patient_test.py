import data
import calendar_test
import history_test


class Patient:
    def __init__(self, fName, lName, address, email, password, phone_number, scheduled_appointments, patient_history):
        self.fName = fName
        self.lName = lName
        self.address = address
        self._email = email
        self._password = password
        self.phone_number = phone_number
        self.scheduled_appointments = scheduled_appointments
        self.patient_history = patient_history

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    def schedule_appointment(self, date, time, gp_email, calendar_list):
        calendar = calendar_list[gp_email]
        calendar.add_entry(date, time, self._email, entry_type="Appointment")

    def cancel_appointment(self, date, time, gp_email, calendar_list):
        calendar = calendar_list[gp_email]
        calendar.remove_entry(date, time)

