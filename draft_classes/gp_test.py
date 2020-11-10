import data
import calendar_test
import history_test


class GP:
    def __init__(self, fName, lName, email, password):
        self.fName = fName
        self.lName = lName
        self._email = email
        self._password = password
    
    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password
        
    def add_calendar_entry(self, date, time, participant_email, entry_type, calendar_list):
        calendar = calendar_list[self._email]
        calendar.add_entry(date, time, participant_email, entry_type)

    def remove_calendar_entry(self, date, time, calendar_list):
        calendar = calendar_list[self._email]
        calendar.remove_entry(date, time)
 
    def add_history_entry(self, c_email, date, time, description, perscription, c_history_list):
        c_history = c_history_list[c_email]
        c_history.add_entry(date, time, c_email, description, perscription, self._email)

    @staticmethod
    def remove_history_entry(c_email, date, time, c_history_list):
        c_history = c_history_list[c_email]
        c_history.remove_entry(date, time)