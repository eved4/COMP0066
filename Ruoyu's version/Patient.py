from User import User
from Appointment import Appointment
from datetime import datetime


class Patient(User):
    def __init__(self, userName, password, title, firstName, lastName, birthDate, gender, telephone, address,
                 medicalHistory):
        super().__init__(userName, password, "patient", title, firstName, lastName, birthDate, gender, telephone, address)
        self.medicalHistory = medicalHistory
        self.appointment = []

    def request_appointment(self, database, medicalWorkerUserName, appointmentDateTimeTuple, reason):
        now = datetime.now()
        appointmentID = now.strftime("%Y%m%d%H%M%S") + self.userName
        result = Appointment(self.userName, medicalWorkerUserName, appointmentDateTimeTuple, reason)

        database["appointment"][appointmentID] = result
        try:
            database["user_confirmed"][medicalWorkerUserName].appointment_waiting[appointmentDateTimeTuple].append(appointmentID)
        except KeyError:
            database["user_confirmed"][medicalWorkerUserName].appointment_waiting[appointmentDateTimeTuple] = [appointmentID]

    def cancel_appointment(self, database, appointmentID):
        appointment_to_cancel = database["appointment"][appointmentID]
        appointment_date_time = appointment_to_cancel.appointmentDateTimeTuple

        if appointment_to_cancel.status == "accepted":
            database["user_confirmed"][appointment_to_cancel.medicalWorkerUserName].availability_confirmed.pop(
                appointment_date_time)
            database["availability"][appointment_to_cancel.medicalWorkerUserName].append(appointment_date_time)
        elif appointment_to_cancel.status == "pending":
            database["user_confirmed"][appointment_to_cancel.medicalWorkerUserName].availability_waiting[appointment_date_time].pop(appointmentID)
        database["appointment"][appointmentID].status = "cancelled"

    def check_appointment(self, database):
        for appointmentID in self.appointment:
            database["appointment"][appointmentID].display_to_patient(database)

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.userName, self.firstName, self.lastName, self.birthDate, self.address, self.telephone)
