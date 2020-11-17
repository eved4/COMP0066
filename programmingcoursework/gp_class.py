# the following code will make classes for GP

# Ive put all the functions within GP and Nurse for Now, but after we discuss it I imagine all the methods will be in a
# calendar class and I'll write a function within doctor to call it for an instance

from reportlab.pdfgen.canvas import Canvas
from sampleCal import Calendar

class GP():


    """
    populate this with data from a database?
    the key is the drug and the symptoms are value?
    """

    def __init__(self, fName, lName, email, password):

        self.fName = fName
        self.lName = lName
        self.email = email
        self._password = password
        self.cal = Calendar()

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    def add_days_appointment_GP(self, start_time, final_slot, date):

        """
        This code effectively creates a days worth of free appointments for the doctor, and adds them to
         a bigger calendar list. The doctor can then customise the calendar by changing the values from free
        to busy, or if a patient takes it, the patients user_id

        """
        return self.cal.add_days_appointment(start_time, final_slot, date)




    def take_days_holiday_GP(self, date):
        """
        Doctor can book themselves a days holiday, removing a full day of slots

        """
        return self.cal.take_day_holiday(date)

    def confirm_space_GP(self, date, time, patientid):
        """
        doctor can book a space at a given date and time by replacing 'free' with the relevant patient ID
        """
        return self.cal.confirm_space(date, time, patientid)

    def prescription_form(self):
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

    def add_patient_history(self, patient_email, description, gp_id, date, time):
        """
        Once I have the patient class, I'll write code that calls a method from it, matching the email and adding to
        the dictionary
        """
    def remove_patient_history(self, patient_email, description, gp_id, date, time):
        """
        same as above, need patient class
        """












