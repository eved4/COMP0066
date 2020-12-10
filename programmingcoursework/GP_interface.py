
import sqlite3
import time
from programmingcoursework.gp_class import GP
from programmingcoursework.prescription import Prescription
from programmingcoursework.medicalinfo import MedicalInfo

from reportlab.pdfgen import canvas

con = sqlite3.connect('/Users/williamsdonlan/Desktop/UniWork/COMP0066/programmingcoursework/gp_server.db')
cur = con.cursor()

def doctor_interface(login_email):
    time.sleep(2)
    print('Welcome to the main program, your options are:')
    time.sleep(2)
    print('Add Availability: 1' + ' ' + 'Check Anonymous Feedback: 2' + ' ' + 'Confirm Appointment: 3' + ' ' +
          'Give Prescription: 4', 'Add Medical History: 5' 'Exit: 0')
    action = input('Enter the number for what you wish to proceed with: ')

    if action == str(0):
        exit()

    elif action == str(1):
        #Not to self: bulk add availability here? Maybe use my old function (need to find)
        pass

    elif action == str(2):
        with con:
            cur.execute("SELECT username FROM doctors WHERE email=?", (login_email,))
            rows = cur.fetchone()

            cur.execute("SELECT score, comment FROM feedback WHERE username=?", (rows[0],))
            rows = cur.fetchall()
            print(rows)

    elif action == str(4):
        # probably need to make better tables here with an actual primary key I can reference, just using this as an example
        new_prescrip = Prescription(patient_id=100)
        new_prescrip.create_script()
        with con:
            query = """UPDATE prescriptions SET scripts = ? WHERE username = ?"""
            data = (new_prescrip, 100)
            cur.execute(query, data)
            time.sleep(2)
            print('prescription updated for user! ')

    elif action == str(5):
        # 100 would be the username of the patient, would probably extract from the doctors list of patients
        info = input('Please input the medical history you would like to add!: ')
        new_med = MedicalInfo(info)
        with con:
            query = """UPDATE users SET medical_info = ? WHERE username =?"""
            data = (new_med, 100)
            print('Medical Info added for user')




     else:
        print('error')

doctor_interface('jd@gmail.com')

con.commit()
con.close()
