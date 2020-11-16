import Appointment
import Person
import datetime


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
        super().__init__(userName, password, title, firstName, lastName, birthDate, gender, telephone, address)
        self.patientID = patientID
        self.medicalHistory = medicalHistory

    def requestAppointment(self, doctorID, appointmentDateTime, reason):
        """
        The funtion to request an appointment to GP.

        :param doctorID: (int)
        :param appointmentDateTime: (datetime.datetime)
        :param reason: (string) the simple description of symptoms of the patient

        :return: (Appointment)
        """
        now = datetime.datetime.now()
        # I use present time + userName as appointmentID
        appointmentID = now.strftime("%Y%m%d%H%M%S") + self.userName
        prescription = ''
        result = Appointment(appointmentID, doctorID, appointmentDateTime, reason, prescription)
        return result

# Where should I cancel the appointment?
    def cancelAppointment(self, gp, appointment):
        gp.calender.removeAppointment(appointment)