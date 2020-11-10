class patient:
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
        return self._email = email


    def get_password(self):
        return self._password

    def set_email(self, password):
        return self._password = email

    def schedule_appointment(self, time, date, gp_email):
        pass

    def cancel_appointment(self, time, date, gp_email):
        pass

