
import sys

users = {'admin': 'password1',
         'gp1': 'password2',
         'patient1': 'password3'}


def login(users, username, password):
    """
    A login function. Takes a username and password and checks them against a provided list of users.

    Parameters
    ----------
    users
    username
    password
    """
    if username in users.keys() and users[username] == password:
        return True
    else:
        return False


def register():
    pass


while True:
    choices = ["login", "register"]
    choice = input("Would you like to login or register? ").lower()
    if choice not in choices:
        continue

    if choice == "login":
        username = ""
        password = ""
        while not login(users, username, password):
            username = input("Please enter your username: ")
            password = input("please enter your password: ")
            print("We couldn't find that username and password combination. Please try again!")

        print("You've logged in successfully {}!".format(username))
        # Maybe some sort of session variable should be initialized on successful login
        break
    elif choice == "register":
        print("you chose to register")
        break
