from datetime import datetime
class Appointment:
    def __init__(self, patientUserName, medicalWorkerUserName, appointmentDateTimeTuple, reason):

        self.patientUserName = patientUserName
        self.medicalWorkerUserName = medicalWorkerUserName
        self.appointmentDateTimeTuple = appointmentDateTimeTuple
        self.prescription = ""
        self.reason = reason
        self.status = "pending"

    def appointment_identifier(self):
        pass

    def display_to_gp(self, database):
        patient = database["user_confirmed"][self.patientUserName]
        print(patient.userName + "\t" + patient.firstName + " " + patient.lastName + "\t" + str(
            self))

    def display_to_patient(self, database):
        medicalWorker = database["user_confirmed"][self.medicalWorkerUserName]
        print(medicalWorker.userName + "\t" + medicalWorker.firstName + " " + medicalWorker.lastName
              + "\t" + str(self))

    def __str__(self):
        from_time, to_time = self.appointmentDateTimeTuple
        time_string = datetime.strftime(from_time, "%m/%d/%Y %H:%M") + "-" + datetime.strftime(to_time, "%H:%M")
        return time_string + "\t" + self.reason+"\t" + "\t" + self.prescription +"\t" + self.status