#from prescription import Prescription
#from sampleCal import Calendar
#from patient import Patient
from Classes.Calendar import Calendar
from Classes.Person import Person


class GP(Person):

    def __init__(self, email, username, password, firstName, lastName, role):
        super().__init__(email, username, password, firstName, lastName, role)
        self.cal = Calendar()

    def add_calendar_entry(self, date, time, patient):
        self.cal.add_entry(date, time, patient)

    def delete_calendar_entry(self, date, time):
        self.cal.remove_entry(date, time)




















