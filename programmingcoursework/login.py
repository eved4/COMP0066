# This code is going to check the database to see if the details given match

import sqlite3

con = sqlite3.connect('/Users/williamsdonlan/Desktop/UniWork/COMP0066/programmingcoursework/gp_server.db')
cur = con.cursor()

logged_in = False


def login(login_email, login_password):

    user_type = input('Please input 1 if you are a doctor, or 0 if you are a patient: ')

    if user_type == 0:
        cur.execute("SELECT email, password FROM users")
        rows = cur.fetchall()
        emails = [a[0] for a in rows]
        passwords = [a[1] for a in rows]
        for i in range(len(emails)):
            if emails[i] == login_email and passwords[i] == login_password:
                print('user logged in!')
            else:
                print('nah')


    elif user_type == 1:
        cur.execute("SELECT email, password FROM doctors")
        rows = cur.fetchall()
        emails = [a[0] for a in rows]
        passwords = [a[1] for a in rows]
        for i in range(len(emails)):
            if emails[i] == login_email and passwords[i] == login_password:
                print('user logged in!')
            else:
                print('nah')

    else:
        print('Login failed')


login('willdonlan8@gmail.com', 'Razorcorn11')


con.commit()
con.close()
