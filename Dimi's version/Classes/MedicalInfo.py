class MedicalInfo():
  def __init__(self, patientID, medicalHistory, appointment):
    self.patientID = patientID
    self.medicalHistory = []
    self.medicalInfo.append(medicalInfo)
    #Need to figure out where appointment is held either within MedicalInfo or Patient
    self.appointment = appointment

  def __str__(self):
    '''How to represent the attributes when being called into string representation'''
    return "Patient ID: " + str(self.patientID) + "\nMedical Info: " + str(self.medicalInfo ) + "\nAppointment: " + str(self.appointment)
  
  def update(self, newMedicalHistoryEntry):
    '''Takes in medicalInfo argument which is appended to the end of the medicalHistory attribute of the class'''
    
    #Try and exception handling here to check that the argument fits the data in the attribute

    #If it is correct update the record
    self.medicalInfo.append(newMedicalHistoryEntry)
    return self.medicalInfo

  def clear_medical_history(self):
    '''Clears the whole medicalHistory of the object'''
    self.medicalHistory = []
    return "Medical History has been cleared for " + str(self.patientID)

  def delete_medical_history():
  '''Deletes a part of the medical history, needs an argument for the position or searches the relevant medical info'''  
  #Exception handling to check if there is a relevant medical info if being searched
    pass

  #Extra functions to handle appointment need to be cleared here

testMedicalInfo = MedicalInfo(1, "Asthma", 1)
print(testMedicalInfo)
