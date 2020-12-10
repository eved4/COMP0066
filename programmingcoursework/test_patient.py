import logging

logging.basicConfig(filename='patient.log', level=logging.INFO, format='%(levelname)s:%(message)s')
from Person import Person
class Patient(Person):


    def __init__(self, userName, password, title, firstName, lastName, birthDate, gender, telephone, address,
                 email):

        super().__init__(userName, password, title, firstName, lastName, birthDate, gender, telephone, address)
        self.email = email

        logging.info('Create patient: {} {}'.format(self.firstName, self.lastName))