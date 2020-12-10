
from utilities import *
from datetime import datetime


def patient_menu(username):
    print("Welcome to the patient menu!")

    while True:
        print("\nPlease select an option by entering its corresponding number. "
              "Your options are: \n1. Account management\n2. Request new appointment"
              "\n3. Cancel appointment\n4. View upcoming appointments\n5. View your records"
              "\n6. Log out")
        # Dictionary of choices, so the correct function can be executed based on user's choice
        choices = {'1': manage_account, '2': request_appointment, '3': cancel_appointment,
                   '4': view_appointments, '5': view_records}
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


def manage_account():
    print("manage account")


def request_appointment(username):
    # Take date as user input and convert to datetime
    # TODO: validate this input
    date = str(input("On which date would you like an appointment? (please enter in yyyy-mm-dd format) "))
    time = str(input("At what time would you like an appointment? Appointments are available in 30-minute intervals,"
                     " e.g. 13:00, 13:30, etc. (please enter in hh:mm format) "))
    date = datetime.date(datetime.strptime(date, "%Y-%m-%d"))
    time = datetime.time(datetime.strptime(time, "%H:%M"))

    # Get the list of all users and loop through them
    users_list = unpickle_data("users_list.txt")
    for user in users_list:
        # If the user is a GP, and is free at the specified time slot, offer the patient to book an appointment
        if users_list[user].role == 'gp':
            sch = users_list[user].cal.schedule
            available_slots = \
                sch[(sch['Date'] == date) & (sch['Time'] == time) & (sch['Appointment'] == 0)][['Date', 'Time']]
            if not available_slots.empty:
                print("We have found an available timeslot with Dr. {} {}:".format(users_list[user].firstName, users_list[user].lastName))
                confirm = str(input("Would you like to request this appointment? (enter Y/N) "))
                if confirm.strip().lower() == "y":
                    patient_name = "{} {}".format(users_list[username].firstName, users_list[username].lastName)
                    users_list[user].cal.add_entry(date, time, username, patient_name)
                    pickle_data('users_list.txt', users_list)
                    break
                else:
                    continue


def cancel_appointment():
    print("cancel appointment")


def view_appointments(username):
    # Get the list of all users and loop through them
    users_list = unpickle_data("users_list.txt")
    print("Here are your upcoming appointments: ")
    for user in users_list:
        # If the user is a GP, print any appointments they have with the patient
        if users_list[user].role == 'gp':
            sch = users_list[user].cal.schedule
            patient_appointment = sch[sch['Patient username'] == username][['Date', 'Time']]
            if not patient_appointment.empty:
                print("-----------------------------------------------"
                      "\nDr. {} {}:".format(users_list[user].firstName, users_list[user].lastName))
                print(patient_appointment.reset_index(drop=True))


def view_records():
    print("view records")
