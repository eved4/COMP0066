
"""
placeholder
"""

class Calendar:
    def __init__(self):
        self.schedule = {}

    def add_entry(self, date_time, entry_title, patient_email=None, entry_type=None):
        self.schedule[str(date_time)] = [entry_title, patient_email, entry_type]

    def update_entry(self, date_time, entry_title, patient_email=None, entry_type=None):
        self.schedule[str(date_time)] = [entry_title, patient_email, entry_type]

    def remove_entry(self, date_time):
        del self.schedule[str(date_time)]
