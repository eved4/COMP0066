#import Classes.Appointments
from Classes.Person import Person
#import datetime
#import logging

#logging.basicConfig(filename='patient.log', level=logging.INFO, format='%(levelname)s:%(message)s')


class Patient(Person):
    """
    This is a class to describe the patient user.
    """
    def __init__(self, email, username, password, first_name, last_name, role):
        super().__init__(email, username, password, first_name, last_name, role)

    """
    def request_appointment(self, medicalWorker, appointmentDateTime, reason):
        try:
            now = datetime.datetime.now()
            # I temporarily use present time + userName as appointmentID
            appointmentID = now.strftime("%Y%m%d%H%M%S") + self.userName
            prescription = ''
            result = Appointment(appointmentID, medicalWorker.ID, appointmentDateTime, reason, prescription)
            Database["Appointment_dict"][appointmentID] = result
            logging.info("Patient {} {} requests an appointment of {} {} at {}".format(self.firstName,
                                                                                       self.lastName,
                                                                                    medicalWorker.firstName,
                                                                                    medicalWorker.lastName,
                                                                                    appointmentDateTime.strftime("%Y-%m-%d %H:%M:%S")))
            return True
        except Exception as e:
            logging.error("Patient {} {} is requesting an appointment of {} {} at {}, but {}".format(self.firstName,
                                                                                       self.lastName,
                                                                                    medicalWorker.firstName,
                                                                                    medicalWorker.lastName,
                                                                                    appointmentDateTime.strftime("%Y-%m-%d %H:%M:%S"),
                                                                                    e))
            return False

    def cancel_appointment(self, appointmentID):

        appointment = Database["Appointment_dict"][appointmentID]
        logging.info("Patient {} {} cancel the appointment of {} {} at {}".format(self.firstName, self.lastName,
                                                                                  appointment.medicalWorker.firstName,
                                                                                  appointment.medicalWorker.lastName,
                                                                                  appointment.appointmentDateTime.strftime("%Y-%m-%d %H:%M:%S")))
        return Database["Appointment_dict"].pop(appointmentID, None)
    """