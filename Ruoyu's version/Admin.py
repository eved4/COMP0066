from User import User
from GP import GP

class Admin(User):
    def __init__(self,userName, password, userType, title, firstName, lastName, birthDate, gender, telephone,
                 address):
        super(Admin, self).__init__(userName, password, userType, title, firstName, lastName, birthDate, gender, telephone,
                 address)

    def create_gp(self, userName, password, title, firstName, lastName, birthDate, gender, telephone,
                 address, database):
        newGP = GP(userName, password, title, firstName, lastName, birthDate, gender, telephone, address,database)
        database["user_confirmed"][userName] = newGP

    def deactivate_account(self, userName, database):
        database["user_confirmed"][userName].accountStatus = "deactivated"

    def remove_gp(self, userName,database):
        return database["user_confirmed"].pop(userName, None)

    def confirm_registration(self, userName, database):
        user = database["user_waiting"].pop(userName)
        database["user_confirmed"][userName] = user