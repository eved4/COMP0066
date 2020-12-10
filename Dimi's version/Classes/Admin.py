
from Classes.Person import Person
#import GP
#import Patient
#import Calendar


class Admin(Person):

    def __init__(self, email, username, password, firstName, lastName, role):
        super().__init__(email, username, password, firstName, lastName, role)
