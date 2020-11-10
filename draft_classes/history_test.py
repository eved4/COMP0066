import data


class ClientHistory:
    def __init__(self, c_email, history={}):
        self.__email = c_email
        self.history = history #dict
    
    def get_email(self):
        return self.__email

    def add_entry(self, date, time, description, perscription, gp_email):
        self.history[str(date)+str(time)] = [(date, time, gp_email), description, perscription]

    def remove_entry(self, date, time):
        del self.history[str(date)+str(time)]