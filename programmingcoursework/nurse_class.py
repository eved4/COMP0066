from programmingcoursework.sampleCal import Calendar1
from programmingcoursework.medicalinfo import MedicalInfo
from programmingcoursework.registration import Patient

from Person import Person


class Nurse(Person):

    def __init__(self, fName, lName, email, password, userName, title, firstName, lastName, birthDate, gender,
                 telephone, address):
        super().__init__(userName, password, title, firstName, lastName, birthDate, gender, telephone, address)
        self.fName = fName
        self.lName = lName
        self.email = email
        self._password = password
        self.cal = Calendar1()
        self.appointments = []
        self.patients = []
        self.medical_info = {}

    def add_patient(self, patient: Patient):
        self.patients.append(patient)

    def add_medical_info(self, patient: Patient, information: MedicalInfo):
        self.medical_info[patient.userName] = information

    def update_information(self, patient: Patient, info: MedicalInfo):
        self.medical_info[patient.userName] = info

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
