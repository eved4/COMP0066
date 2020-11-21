"""
placeholder
"""

class Prescription():

    def __init__(self, patient_id):
        self.patient_id = patient_id

    def create_script(self):
        """
        Saves the relevant prescription details in a canvas PDF form,
        the doctor will then print the form and sign it before handing it to
        the patient directly
        (This is a work in progress, would like some suggestions
        for this bit)

        """

        canvas = Canvas("Prescription.pdf")
        canvas.setFont("Times-Roman", 12)

        patient_name = input("Please enter patient name: ")
        patient_DOB = input("Please enter patient Date of Birth: ")
        patient_symptoms = input("Please enter the patient symptoms: ")
        drug = input("Please enter the drug you are prescribing: ")
        dosage = input("Please enter the dosage: ")

        canvas.drawString(72, 500, patient_name)
        canvas.drawString(72, 430, patient_DOB)
        canvas.drawString(72, 360, patient_symptoms)
        canvas.drawString(72, 290, drug)
        canvas.drawString(72, 220, dosage)
        canvas.drawString(200, 150, "Please sign here: ")

        canvas.save()
