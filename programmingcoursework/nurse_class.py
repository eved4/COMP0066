from sampleCal import Calendar
from patient import Patient

class Nurse():

    def __init__(self, fName, lName, email, password):

        self.fName = fName
        self.lName = lName
        self.email = email
        self._password = password
        self.cal = Calendar()
        self.appointments = []
        self.patients = []
        self.medical_info = {}

    def add_patient(self, patient: Patient):
        self.patients.append(patient)

    def add_medical_info(self, patient: Patient, information: MedicalInfo):
        self.medical_info[patient.name] = information

    def update_information(self, patient: Patient, info: MedicalInfo):
        self.medical_info[patient.name] = info

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    def add_calendar_entry(self, date_time, entry_title, patient_email=None, entry_type=None):
        return self.cal.add_entry(date_time, entry_title, patient_email, entry_type)

    def delete_calendar_entry(self, date_time):
        return self.cal.remove_entry(date_time)

    def update_calendar_entry(self, date_time):
        return self.update_calendar_entry(date_time)



