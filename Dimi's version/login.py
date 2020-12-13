
import re
import time
from Classes.Patient import Patient
from Classes.GP import GP
from Classes.Admin import Admin
from utilities import *


def login(username, password):
    # Load the list of users from the pickled file
    users_list = unpickle_data("users_list.txt")

    if username in users_list.keys():
        if users_list[username].password == password:
            return True
    else:
        return False


def login_page():

    while True:
        username = str(input("Please enter your username: "))
        password = str(input("Please enter your password: "))
        if not login(username, password):
            print("We couldn't find that username and password combination. Please try again!")
            continue
        break

    print("You've logged in successfully {}!".format(username))
    return username


def register_account(email, username, password, first_name, last_name, role):
    # Load the list of users from the pickled file
    users_list = unpickle_data("users_list.txt")

    # Check if email is a valid email
    email_pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if len(re.findall(email_pattern, email)) != 1:
        print("You've entered an invalid email address! Please try again")
        return False
    # Check if email is unique
    for key in users_list.keys():
        if users_list[key].email == email:
            print("The email you've entered is already in use! Please enter another email.")
            return False

    # Check if username is unique and between 6 to 20 characters
    username_pattern = re.compile(r"^[a-zA-z0-9_.]{6,20}$")
    if len(re.findall(username_pattern, username)) != 1:
        print("You've entered an invalid username! Your username must be 6-20 characters long, "
              "and must contain only letters, numbers, underscores (_) and dots (.)")
        return False
    elif username in users_list.keys():
        print("The username you've entered is already in use! Please choose another username.")
        return False

    # Check if password is at least 6 characters
    password_pattern = re.compile(r"^.{6,}$")
    if len(re.findall(password_pattern, password)) != 1:
        print("You've entered an invalid password! Your password must be at least 6 characters long.")
        return False

    # Only check if first and last name are not empty
    if len(first_name.strip()) == 0 or len(last_name.strip()) == 0:
        print("You haven't entered a first or last name! First and last name must not be empty.")
        return False

    # If all the input is valid, create a new user object
    if role == "patient":
        new_account = Patient(email, username, password, first_name, last_name, role)
    elif role == "gp":
        new_account = GP(email, username, password, first_name, last_name, role)
    users_list[username] = new_account

    # Pickle the list of patients into a file
    pickle_data("users_list.txt", users_list)

    return True


def register_page(role):

    while True:
        email = input("Please enter an email: ")
        username = str(input("Please enter a username (6-20 characters long, "
                             "and must contain only letters, numbers, underscores (_) and dots (.)): "))
        password = str(input("Please enter a password (at least 6 characters long): "))

        while True:
            password_confirm = str(input("Please confirm the password: "))
            if password != password_confirm:
                print("The password doesn't match! Please try again")
                continue
            break

        first_name = input("Please enter a first name: ")
        last_name = input("Please enter a last name: ")

        if not register_account(email, username, password, first_name, last_name, role):
            print("Your registration was not completed. Please validate your input and try again!")
            continue

        break

    print("Account {} has been registered successfully!".format(username))
