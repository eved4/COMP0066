#from datetime import date


class Person:
    """
    This is a class to describe basic common features of a user.

    """

    def __init__(self, email, username, password, firstName, lastName, role):
        """
        The constructor for Person class.
        """
        self.email = email
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.role = role

    #@property
    #def age(self):
    #    """
    #    The funtion to calculate the age of the user(with property annotation, age is treated as one of attributes).
    #    """
    #    today = date.today()
    #    result = today.year - self.birthDate.year - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day))
    #    return result

    def edit_info(self, attribute_name, new_value):
        """
        The function to edit attributes of the user.
        """
        setattr(self, attribute_name, new_value)



