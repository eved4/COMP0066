
import sys
import time
from utilities import *
from login import *
from admin_menu import *
from gp_menu import *
from patient_menu import *


print("Welcome to University College Hospital's eHealth Management System!")
time.sleep(1)
while True:
    username = ""
    # Load the list of users from the pickled file
    users_list = unpickle_data("users_list.txt")

    # Give user menu of options
    choices = ["1", "2", "3"]
    choice = input("Please select an option: \n1. Log in \n2. Register \n3. Exit\n")
    if choice not in choices:
        continue

    if choice == "1":  # Log in
        username = login_page()
        time.sleep(1)

        if users_list[username].role == 'admin':
            admin_menu()
            continue

        elif users_list[username].role == 'gp':
            gp_menu(username)
            continue

        elif users_list[username].role == 'patient':
            patient_menu(username)
            continue

        break

    elif choice == "2":  # Register
        # Only patients can register, GP's are added by admins
        register_page('patient')
        continue

    elif choice == "3":  # Exit
        print("Thank you for using eHealth! Bye bye :)")
        sys.exit()
