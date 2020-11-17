from sampleCal import Calendar

"""
need a bit more info on how we are doing the calendar before i can make a referral method
"""

class Nurse():

    def __init__(self, fName, lName, email, password):
        self.fName = fName
        self.lName = lName
        self.email = email
        self._password = password
        self.cal = Calendar()

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    def add_days_appointment_GP(self, start_time, final_slot, date):
        """
        This code effectively creates a days worth of free appointments for the doctor, and adds them to
         a bigger calendar list. The doctor can then customise the calendar by changing the values from free
        to busy, or if a patient takes it, the patients user_id

        """
        return self.cal.add_days_appointment(start_time, final_slot, date)

    def take_days_holiday_GP(self, date):
        """
        Doctor can book themselves a days holiday, removing a full day of slots

        """
        return self.cal.take_day_holiday(date)

    def confirm_space_GP(self, date, time, patientid):
        """
        doctor can book a space at a given date and time by replacing 'free' with the relevant patient ID
        """
        return self.cal.confirm_space(date, time, patientid)

    def add_patient_history(self, patient_email, description, gp_id, date, time):
        """
        Once I have the patient class, I'll write code that calls a method from it, matching the email and adding to
        the dictionary
        """
    def remove_patient_history(self, patient_email, description, gp_id, date, time):
        """
        same as above, need patient class
        """

    def make_referal(self, date, time):
        """
        need to fix this: will parse over the bigger calendar, looking for free sessions given a specified date/time by
        the patient
        """



