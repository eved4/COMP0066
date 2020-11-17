
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
    def add_gp(first_name, last_name, email, password, gp_list, calendar_list):
        """
        Placeholder code. This method would create a GP object and set it to inactive initially.
        The admin can then activate/deactivate the account as needed with the other methods.
        """
        gp = GP(first_name, last_name, email, password)
        gp_list[email] = gp

        calendar = Calendar(email)
        calendar_list[email] = calendar

    @staticmethod
    def remove_gp(gp, email, gp_list, calendar_list):
        """
        Placeholder code. This method should delete the GP object and all GP details from the directory.
        """
        del gp
        del gp_list[email]
        del calendar_list[email]

    @staticmethod
    def activate_gp(first_name, last_name, email, password, gp_list, calendar_list):
        """
        Placeholder code. This method should set an existing GP account to active.
        """
        gp_list[email] = 1
    
    @staticmethod
    def deactivate_gp(email, gp_list):
        """
        Placeholder code. This method should set an existing GP account to inactive and not delete it.
        """
        gp_list[email] = 0

    @staticmethod
    def confirm_patient(email, patients_list):
        """
        Placeholder code. When a patient registers, their details are entered into a patient directory.
        Initially, their account is set to inactive and this method would set the account to active.
        """
        patients_list[email] = 1
