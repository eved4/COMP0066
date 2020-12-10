from database import database
import pickle
from MedicalWorker import MedicalWorker
from Patient import Patient

print("Welcome to COMP0066 system!\n")
login = False
while not login:
    option = int(input("1. login\n2. register\n3. exit\nPlease choose the number of the action you want to take[1-3]:\n"))
    if option == 1:
        while not login:
            userName = input("username:\n")
            password = input("password:\n")
            try:
                user = database["user_confirmed"][userName]
                if user.password == password:
                    login = True
                    userType = user.userType
                else:
                    flag = input("Wrong username or password, do you want to try again?(Y/N)\n")
                    if flag != 'Y':
                        break
            except KeyError:
                try:
                    user = database["user_waiting"][userName]
                    flag = input("Waiting for confirmation of admin, thank you for your patience!\n"
                                 "Do you want to try again?(Y/N)\n")
                    if flag != 'Y':
                        break
                except KeyError:
                    print("You are not registered!")
    elif option == 2:
        print("Please enter following information:")
        # userName, password, userType, title, firstName, lastName, birthDate, gender, telephone,address
        userName = input("(1/9)username:\n")
        password = input("(2/9)password:\n")
        userType = "patient"
        title = input("(3/9)title:\n")
        firstName = input("(4/9)first name:\n")
        lastName = input("(5/9)last name:\n")
        birthDate = input("(6/9)birthDate(eg. 09/30/1997):\n")
        gender = input("(7/9)gender:\n")
        telephone = input("(8/9)telephone:\n")
        address = input("(9/9)address:\n")
        new_patient = Patient(userName, password, title, firstName, lastName, birthDate, gender, telephone,address, "")
        database["user_waiting"][userName] = new_patient
        print("\t\t\t\t***Congratulations!***\n"
              "You have finished the registration form, please wait for the confirmation of system admin.")
    elif option == 3:
        break

while login:
    while userType == "admin" and login:
        print("1. add new gp\n2. deactivate gp\n3. delete gp\n4.confirm patient's registration\n5. manage patients records\n6.logout")
        option = int(input("Please choose the things you want to do[1-6]:\n"))
        if option == 1:
            print("Please enter following information:")
            userName = input("(1/9)username:\n")
            password = input("(2/9)password:\n")
            userType = "patient"
            title = input("(3/9)title:\n")
            firstName = input("(4/9)first name:\n")
            lastName = input("(5/9)last name:\n")
            birthDate = input("(6/9)birthDate(eg. 09/30/1997):\n")
            gender = input("(7/9)gender:\n")
            telephone = input("(8/9)telephone:\n")
            address = input("(9/9)address:\n")

            user.create_gp(userName, password, title, firstName, lastName, birthDate, gender,
                           telephone, address, database)
            print("You have add a new gp("+userName + ") to user table!")

        elif option == 2:
            targetUser = input("Please input the username you want to deactivate:\n")
            user.deactivate_account(targetUser, database)
        elif option == 3:
            targetUser = input("Please input the username of gp you want to remove:\n")
            user.remove_gp(targetUser,database)
        elif option == 4:
            for i,j in database["user_waiting"].items():
                print(i+": "+str(j))
            targetUser = input("Please input the username you want to confirm:\n")
            user.confirm_registration(targetUser, database)
            print("You have confirmed the user:" + targetUser)
        elif option == 5:
            pass
        elif option == 6:
            login = False

    while userType == "gp" and login:
        print("1. add availability\n2. confirm appointment\n3. input prescription\n4.logout")
        option = int(input("Please choose the things you want to do[1-4]:\n"))
        if option == 1:
            availability = input("Please input the availability, for example: 09/30/2020 12:30-13:30\n")
            user.add_availability(availability,database)
        elif option == 2:
            mapping_id = user.display_appointment_waiting(database)
            if len(mapping_id) == 0:
                print("No waiting appointment!")
            else:
                appointmentID_to_confirm = int(input("Please enter the number of appointment you want to confirm:\n"))
                user.confirm_appointment(mapping_id[appointmentID_to_confirm - 1], database)
                print("You have confirmed the following appoint:\n")
                database["appointment"][mapping_id[appointmentID_to_confirm - 1]].display_to_gp(database)
        elif option == 3:
            mapping_id = user.display_appointment_confirmed(database)
            appointmentID_to_edit = int(input("Please input the No. of the appointment whose prescription you want to edit:\n"))
            prescription = input("Please write your prescription:\n")
            user.add_prescription(mapping_id[appointmentID_to_edit - 1], database, prescription)
        elif option == 4:
            login = False

    while userType == "nurse" and login:
        pass

    while userType == "patient" and login:
        print("1. book appointment\n2. cancel appointment\n3. check appointment\n4.logout")
        option = int(input("Please choose the things you want to do[1-4]:\n"))
        if option == 1:
            mapping = []
            number_gp = 1
            for gp, availability_list in database["all_availability"].items():
                print(number_gp, end=". ")
                print(database["user_confirmed"][gp].firstName, database["user_confirmed"][gp].lastName)
                mapping.append(gp)
                for availability in availability_list:
                    print("\t", end="")
                    number_avail = 1
                    print(number_avail, end=". ")
                    MedicalWorker.print_availability(availability)
                    number_avail += 1
                number_gp += 1
            chosen_gp, chosen_availability_number = input("Please input the identifier of gp and the number of availability"
                                                   " (for example:1 2):\n").split()
            reason = input("Please enter the reason of booking an appointment:")
            chosen_gp_userName = mapping[int(chosen_gp)-1]
            chosen_availability = database["all_availability"][chosen_gp_userName][int(chosen_availability_number)-1]
            user.request_appointment(database, chosen_gp_userName, chosen_availability , reason)
        elif option == 2:
            pass
        elif option == 3:
            user.check_appointment(database)
        elif option == 4:
            login = False

dbfile = open("database", "wb")
pickle.dump(database, dbfile)
dbfile.close()
print("bye")
