
from utilities import *


def gp_menu(username):
    print("Welcome to the GP menu!")

    while True:
        print("\nPlease select an option by entering its corresponding number. "
              "Your options are: \n1. View upcoming appointments\n2. Adjust your availability"
              "\n3. Manage appointment requests\n4. Update patient records\n5. Add prescription"
              "\n6. Log out")
        # Dictionary of choices, so the correct function can be executed based on user's choice
        choices = {'1': view_appointments, '2': adjust_availability, '3': manage_appointments,
                   '4': update_patient_record, '5': add_prescription}
        choice = input()
        if choice == "6":
            print("You've logged out successfully!")
            break
        elif choice in choices.keys():
            choices[choice](username)
            continue
        else:
            print("You've selected an invalid option. Please try again!")
            continue


def view_appointments(username):
    users_list = unpickle_data("users_list.txt")
    schedule = users_list[username].cal.schedule
    print(schedule[schedule['Appointment'] == 1])


def adjust_availability(username):
    print("adjust availability")


def manage_appointments(username):
    print("manage appointments")


def update_patient_record(username):
    print("update patient record")


def add_prescription(username):
    print("add prescription")
