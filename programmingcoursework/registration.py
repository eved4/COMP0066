import logging
import datetime
from programmingcoursework.test_patient import Patient

import sqlite3

con = sqlite3.connect('/Users/williamsdonlan/Desktop/UniWork/COMP0066/programmingcoursework/gp_server.db')
cur = con.cursor()

logging.basicConfig(filename='patient.log', level=logging.INFO, format='%(levelname)s:%(message)s')


class MedicalInfo():
    def __init__(self, information):
        self.information = information

    def update_info(self, new_information):
        self.information = new_information


def registration():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    title = input("Please enter your title: ")
    fname = input("Please enter your first name: ")
    lname = input("Please enter your last name: ")
    DOB1 = datetime.date(1997, 1, 1)
    gender = input("Please enter your gender: ")
    telephone1 = input("Please enter your number: ")
    address1 = input("Please enter your address: ")
    email1 = input("Please enter your email: ")
    med_hist = input("Please enter any relevant medical history: ")

    new_patient = Patient(username, password, title, fname, lname, DOB1, gender, telephone1, address1, email1)
    med_hist_class = MedicalInfo(med_hist)
    with con:
        try:
            cur.execute("SELECT email FROM users WHERE email=:email", {'email': email1})
            print('email already taken, please try again')
        except:
            cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",
                        (new_patient.firstName, new_patient.lastName, new_patient.age,
                         new_patient.email, med_hist_class.information, new_patient.password))

            con.commit()

            print('user registered! you are ready to login')


registration()

con.commit()
con.close()

"""
The user will input the information necessary to make a patient class. Checked to see if it works, if so, inserted into DB
"""
