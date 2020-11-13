
import data
from gp_test import GP
from patient_test import Patient
from calendar_test import Calendar
from history_test import ClientHistory


class Admin:
    """
    An Admin class...
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def activate_gp(first_name, last_name, email, password, gp_list, calendar_list):
        """ Do GP's register themselves, or does the admin add GP accounts?
        If the latter, this method should be changed to add_gp, where we create a GP object
        and set it to active. If the former, then GP's would register like patients
        and their details entered into a GP directory as an inactive account, and this
        method would just set the account to active."""

        gp = GP(first_name, last_name, email, password)
        gp_list[email] = gp

        calendar = Calendar(email)
        calendar_list[email] = calendar
    
    @staticmethod
    def deactivate_gp(email, gp_list):
        """Placeholder code. This method should just set the GP account to inactive and not delete it."""
        gp_list[email] = 0

    @staticmethod
    def remove_gp(email, gp_list, calendar_list):
        """This method should delete all GP details."""
        del gp_list[email]
        del calendar_list[email]

    @staticmethod
    def confirm_patient(email, patients_list):
        """When a patient registers, their details are entered into a patient directory.
        Initially, their account is set to inactive and this method would set the account
        to active; below code is just placeholder"""
        patients_list[email] = 1
    # ...

        
