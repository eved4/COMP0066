from MedicalWorker import MedicalWorker


class GP(MedicalWorker):
    def __init__(self, userName, password, title, firstName, lastName, birthDate, gender, telephone,
                 address, database):
        super(GP, self).__init__(userName, password, "gp", title, firstName, lastName, birthDate, gender, telephone,
                 address, database)

    def add_prescription(self,appointmentID, database, prescription):
        database["appointment"][appointmentID].prescription = prescription
        database["appointment"][appointmentID].status = "finished"
        self.appointment_confirmed.pop(database["appointment"][appointmentID].appointmentDateTimeTuple)
        self.appointment_finished.append(appointmentID)
