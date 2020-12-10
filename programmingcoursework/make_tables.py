import sqlite3
from programmingcoursework.gp_class import GP
import datetime

con = sqlite3.connect('/Users/williamsdonlan/Desktop/UniWork/COMP0066/programmingcoursework/gp_server.db')
cur = con.cursor()

"""
patients table: This includes the medical history they are initialised with
"""
# patients_sql = """
# CREATE TABLE users (
# first_name text,
# last_name text,
# age integer,
# email text,
# medical_history text,
# password text)"""

# prescriptions_sql = """
# CREATE TABLE prescriptions (
# username text PRIMARY KEY,
# scripts text)"""
# cur.execute(prescriptions_sql)
# con.commit()
# con.close()


# doctors_sql = """
# CREATE TABLE doctors (
# username text PRIMARY KEY,
# first_name text,
# last_name text,
# age integer,
# email text,
# password text)"""
# cur.execute(doctors_sql)
#
# doc_cal_sql = """
# CREATE TABLE calendar (
# username text,
# available_days text,
# FOREIGN KEY (username) REFERENCES doctors (username))"""

# doc_feedback = """
# CREATE TABLE feedback (
# username text,
# score integer,
# comment text,
# FOREIGN KEY (username) REFERENCES doctors (username))"""
#
# cur.execute(doc_feedback)
# con.commit()
# con.close()

#
# DOB = datetime.datetime(2020, 2, 2)
# test_gp = GP('jd@gmail.com', 'Razorcorn11', 'johndoe', 'Mr', 'John', 'Doe', DOB, 'male', 'NA', 'NA')
#
# with con:
#     cur.execute("INSERT INTO doctors VALUES (?, ?, ?, ?, ?, ?)",
#                 (test_gp.userName, test_gp.firstName, test_gp.lastName,
#                  test_gp.age, test_gp.email, test_gp.password))
#
#     con.commit()




