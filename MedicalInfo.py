class MedicalInfo():
  def __init__(self, patientID, medicalInfo, appointment):
    self.patientID = patientID
    self.medicalInfo = []
    self.medicalInfo.append(medicalInfo)
    self.appointment = appointment

  def __str__(self):
    return "Patient ID: " + str(self.patientID) + "\nMedical Info: " + str(self.medicalInfo ) + "\nAppointment: " + str(self.appointment)
  
  def update(self, medicalInfo):
    self.medicalInfo.append(medicalInfo)
    return self.medicalInfo
  
testMedicalInfo = medicalInfo(1, "Asthma", 1)
print(testMedicalInfo)
