#Appointment
#Parameters(appointmentID, doctorID, patientID, appointmentDateTime, reason, prescription)

import Patient
import GP
#import Database

'''Retrieve patientID from Patient class and medicalWorkerID from GP class.'''

class Appointment(Patient, GP):
    def __init__(self, medicalWorkerID, patientID, appointmentID, appointmentDateTime, reason, prescription):
        Patient.__init__(self, patientID)
        GP.__init__(self, medicalWorkerID)
        self.appointmentID = appointmentID
        self.appointmentDateTime = appointmentDateTime
        self.reason = reason
        self.prescription = prescription



