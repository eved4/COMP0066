
import Person
import GP
import Patient
import Calendar


class Admin(Person):
    """
    This is a class to describe the admin user.

    Attributes:
        username(string)
        password(string)
        title(string)
        first_name(string)
        last_name(string)
        birth_date(datetime.date)
        gender(string)
        telephone(string)
        address(string)
    """
    def __init__(self, username, password, title, first_name, last_name, birth_date, gender, telephone, address):
        """
        The constructor for the Admin class.

        Parameters
        ----------
        username
        password
        title
        first_name
        last_name
        birth_date
        gender
        telephone
        address
        """
        Person.__init__(self, username, password, title, first_name, last_name, birth_date, gender, telephone, address)

    @staticmethod
    def activate_account(email, users_list):
        """
        Placeholder code. This method will activate any account - GP or patient.
        """
        users_list[email] = 1

    @staticmethod
    def deactivate_account(email, users_list):
        """
        Placeholder code. This method will deactivate any account - GP or patient.
        """
        users_list[email] = 0

    @staticmethod
    def add_gp(first_name, last_name, email, password, gp_list, calendar_list):
        """
        Placeholder code. This method would create a GP object and set it to inactive initially.
        The admin can then activate/deactivate the account as needed with the other methods.
        """
        gp = GP(first_name, last_name, email, password)
        gp_list[email] = gp

        calendar = Calendar(email)
        calendar_list[email] = calendar

    @staticmethod
    def remove_gp(gp, email, gp_list, calendar_list):
        """
        Placeholder code. This method should delete the GP object and all GP details from the directory.
        """
        del gp
        del gp_list[email]
        del calendar_list[email]

