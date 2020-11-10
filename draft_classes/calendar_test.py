import data


class Calendar:
    def __init__(self, gp_email, schedule={}):
        self.__email = gp_email
        self.schedule = schedule #dict
    
    def get_email(self):
        return self.__email

    def add_entry(self, date, time, participant_email, entry_type=None):
        self.schedule[str(date)+str(time)] = [(date, time), participant_email, entry_type]

    def remove_entry(self, date, time):
        del self.schedule[str(date)+str(time)]