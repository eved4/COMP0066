import Appointment
import Person
import datetime
import logging

logging.basicConfig(filename='patient.log', level=logging.INFO, format='%(levelname)s:%(message)s')


class Patient(Person):
    """
    This is a class to describe the patient user.

    Attributes:
        userName(string)
        password(string)
        title(string)
        firstName(string)
        lastName(string)
        birthDate(datetime.date)
        gender(string)
        telephone(string)
        age(int)
        address(string)
        patientID(int)
        medicalHistory(MedicalInfo)
    """
    def __init__(self, userName, password, title, firstName, lastName, birthDate, gender, telephone, address, patientID,
                 medicalHistory):
        """
        The constructor of Patient class.

        :param userName: (string)
        :param password: (string)
        :param title: (string)
        :param firstName: (string)
        :param lastName: (string)
        :param birthDate: (datetime.date)
        :param gender: (string)
        :param telephone: (string)
        :param address: (string)
        :param patientID: (int)
        :param medicalHistory: (MedicalInfo)
        """
        Person.__init__(userName, password, title, firstName, lastName, birthDate, gender, telephone, address)
        self.patientID = patientID
        self.medicalHistory = medicalHistory

        logging.info('Create patient: {} {}'.format(self.firstName,self.lastName))

    def request_appointment(self, medicalWorker, appointmentDateTime, reason):
        """
        The function to request an appointment to GP.

        :param medicalWorker: (MedicalWorker)
        :param appointmentDateTime: (datetime.datetime)
        :param reason: (string) the simple description of symptoms of the patient

        :return: (Appointment)
        """
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
        """
        Ther function to cancle an appointment by appointment id.

        :param appointmentID: (int)
        :return: if appointment id exists, return corresponding appoint, otherwise None
        """
        appointment = Database["Appointment_dict"][appointmentID]
        logging.info("Patient {} {} cancel the appointment of {} {} at {}".format(self.firstName, self.lastName,
                                                                                  appointment.medicalWorker.firstName,
                                                                                  appointment.medicalWorker.lastName,
                                                                                  appointment.appointmentDateTime.strftime("%Y-%m-%d %H:%M:%S")))
        return Database["Appointment_dict"].pop(appointmentID, None)
