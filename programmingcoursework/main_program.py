"""
The main menu of the program (I suppose will we use click to display it all properly
"""
import sqlite3
import time
from programmingcoursework.feedback import Feedback

con = sqlite3.connect('/Users/williamsdonlan/Desktop/UniWork/COMP0066/programmingcoursework/gp_server.db')
cur = con.cursor()

def user_interface(login_email):
    time.sleep(2)
    print('Welcome to the main program, your options are:')
    time.sleep(2)
    print('Book Appointment: 1' + ' ' + 'Check Medical History: 2' + ' ' + 'Give Feedback: 3 ' + ' ' + 'Exit: 0')
    action = input('Enter the number for what you wish to proceed with: ')

    if action == str(0):
        exit()
    elif action == str(2):
        print('Displaying Medical History....')
        time.sleep(2)
        # code to grab the medical history for a specific
        with con:
            cur.execute("SELECT medical_history FROM users WHERE email=?", (login_email,))
            rows = cur.fetchall()

            for row in rows:
                print(row)

    elif action == str(1):
        #book appointment
        #pick a doctor then search through all their availibility
        print('Select which doctor you wish to see- Will Donlan: 1')
        time.sleep(2)
        chosen_doc = input('Please enter the doctor integer here: ')

        if chosen_doc == str(1):
            cur.execute("SELECT availability FROM calendar WHERE username=?", ('johndoe',))
            rows = cur.fetchall()
            for row in rows:
                print(row)
            # havent got to this bit yet, something like, the user chooses an appointment and an email
            # is sent to the GP and admin to approve, or admin gets a notification on their homepage

    elif action == str(3):
        print('Select which doctor you wish to give feedback on- Will Donlan: 1')
        time.sleep(3)
        chosen_doc = input('Please enter the doctor integer here: ')

        if chosen_doc == str(1):
            rating = input('What would you give your appointment out of 5?')
            comment = input('Do you have a comment about the doctor?')
            doc_feedback = Feedback(rating, comment)
            with con:
                cur.execute("INSERT INTO feedback VALUES (?, ?, ?)", ('willdonlan', doc_feedback.score, doc_feedback.comment))
                con.commit()
                time.sleep(2)
                print('Feedback given')


    else:
        print('Error occurred, please try again or select 0 to exit: ')


user_interface('willdonlan8@gmail.com')

con.commit()
con.close()
