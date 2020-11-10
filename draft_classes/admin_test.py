import data
from gp_test import GP
from patient_test import Patient
from calendar_test import Calendar
from history_test import ClientHistory


class Admin:  
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def activateGP(fName, lName, email, password, gp_list, calendar_list):
        gp = GP(fName, lName, email, password)
        gp_list[email] = gp

        calendar = Calendar(email)
        calendar_list[email] = calendar
    
    @staticmethod
    def deactivateGP(email, gp_list, calendar_list):
        del gp_list[email]
        del calendar_list[email]

    # ...

        
