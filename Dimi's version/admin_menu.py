
import time
from login import register_page
from utilities import *


def admin_menu():
    print("Welcome to the admin menu!")

    while True:
        print("\nPlease select an option by entering its corresponding number. "
              "Your options are: \n1. Add GP account\n2. Remove GP account"
              "\n3. Activate account\n4. Deactivate account\n5. Confirm patient registration"
              "\n6. Log out")
        # Dictionary of choices, so the correct function can be executed based on user's choice
        choices = {'1': add_gp, '2': remove_gp, '3': activate_account, '4': deactivate_account,
                   '5': confirm_patient}
        choice = input()
        if choice == "6":
            print("You've logged out successfully!")
            break
        elif choice in choices.keys():
            choices[choice]()
            continue
        else:
            print("You've selected an invalid option. Please try again!")
            continue


def add_gp():
    print("You've selected the option to add a new GP account.")
    time.sleep(1)
    register_page('gp')


def remove_gp():
    print("You've selected the option to remove a GP account.")
    # Load the list of users from the pickled file
    users_list = unpickle_data("users_list.txt")

    while True:
        # Get GP username from user and delete from the list
        gp_username = str(input("Please enter the username of the GP you would like to remove: "))
        if gp_username not in users_list.keys():
            print("We couldn't find that account! Please try again.")
            continue
        confirm = str(input("Are you sure you want to delete this GP account? "
                            "This action cannot be reversed. (Enter Y or N) "))
        if confirm.lower().strip() == "y":
            del users_list[gp_username]
            print("GP account {} was removed successfully.".format(gp_username))
            break
        else:
            print("GP account was not removed.")
            break

    # Pickle the list of patients into a file
    pickle_data("users_list.txt", users_list)


def activate_account():
    print("activate account")


def deactivate_account():
    print("deactivate account")


def confirm_patient():
    print("confirm patient")
