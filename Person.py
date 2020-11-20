from datetime import date


class Person:
    """
    This is a class to describe basic common features of a user.

    Attributes:
        userName(string)
        password(string)
        title(string)
        firstName(string)
        lastName(string)
        birthDate(datetime.date)
        gender(string)
        telephone(string)
        age(int)
        address(string)
    """

    def __init__(self, userName, password, title, firstName, lastName, birthDate, gender, telephone, address):
        """
        The constructor for Person class.
        """
        self.userName = userName
        self.password = password
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.gender = gender
        self.telephone = telephone
        self.address = address

    @property
    def age(self):
        """
        The funtion to calculate the age of the user(with property annotation, age is treated as one of attributes).
        """
        today = date.today()
        result = today.year - self.birthDate.year - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day))
        return result

    def edit_info(self, attributeName, newValue):
        """
        The function to edit attributes of the user.

        :param attributeName: (string) the name of the attribute to be changed
        :param newValue: (the type of the attribute to be changed) the new value of the attribute

        :return: None
        """
        setattr(self, attributeName, newValue)



