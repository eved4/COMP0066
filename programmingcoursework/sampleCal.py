from datetime import datetime, timedelta



class Calendar():

    """
    This is just a placemarker Calendar until 17/11/20 - can discuss implementation then. It only contains the
    relevant features for the GP class. The GP will add to the calendar the days they are free, and it will generate
    30 minute time slots. They can then manually remove a slot, or assign a slot to a patient. Patients will parse
    through available slots and select one, which is then confirmed by GP
    """

    def __init__(self):
        self.schedule = {}


    def add_days_appointment(self, start_time, final_slot, date):

        start = datetime.strptime(start_time, '%H:%M')
        end = datetime.strptime(final_slot, '%H:%M')

        appointment_length = 30
        day_appointment_cal = {}

        while start < end:
            day_appointment_cal[start.strftime("%H:%M")] = 'free'
            start = start + timedelta(minutes=appointment_length)

        self.schedule[date] = day_appointment_cal
        return self.schedule


    def take_day_holiday(self, date):
        del self.schedule[date]
        return self.schedule

    def confirm_space(self, date, time, patient_email):
        """
        doctor can book a space at a given date and time by replacing 'free' with the relevant patient ID
        """
        self.schedule[date][time] = patient_email
