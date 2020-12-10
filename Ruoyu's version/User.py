from datetime import date


class User:
    def __init__(self, userName, password, userType, title, firstName, lastName, birthDate, gender, telephone,
                 address, accountStatus = "activated"):
        self.userName = userName
        self.password = password
        self.userType = userType
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.gender = gender
        self.telephone = telephone
        self.address = address
        self.accountStatus = accountStatus

    @property
    def age(self):
        today = date.today()
        result = today.year - self.birthDate.year - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day))
        return result

    def edit_info(self, attributeName, newValue):
        setattr(self, attributeName, newValue)

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.userName, self.firstName, self.lastName, self.birthDate, self.address, self.telephone)