import tkinter as tk
from tkinter import *
from tkcalendar import *
#import GPList

GP = ["Dr. Johnson", "Dr. James", "Dr. Young", "Dr. Lee", "Dr. Miller"]


def submitReasons():
    tk.Label(top, text="You just submitted your reasons for appointment. The GP will receive it soon.").pack()
    file_name = entry.get()
    with open('appointments.txt', 'a', newline="") as file_object:
        file_object.write(file_name)




def selectGP():
    tk.Label(top, text=clicked.get()).pack()
    insertGP = clicked.get()
    with open('appointments.txt', 'a', newline="") as file_insertGP:
        file_insertGP.write(insertGP)




def getCalendar():
    dateLabel = Label(top, text="")
    dateLabel.pack(pady=20)
    dateLabel.config(text="Confirmed! Your appointment is on: " + timetable.get_date())
    insertDate = timetable.get_date()
    with open('appointments.txt', 'a', newline="") as file_insertDate:
        file_insertDate.write(insertDate)




if __name__ == '__main__':
    top = tk.Tk()
    top.title("Book Appointment!")
    entry_field_variable = tk.StringVar()
    entry = tk.Entry(top, textvariable=entry_field_variable)
    entry.pack()
    tk.Button(top, text="Please submit reasons/symptoms for appointment", command=submitReasons).pack()
    clicked = StringVar()
    clicked.set(GP[0])
    tk.OptionMenu(top, clicked, *GP).pack()
    tk.Button(top, text="Please select a GP", command=selectGP).pack()
    timetable = Calendar(top)
    timetable.pack(pady=20)
    tk.Button(top, text="Choose eligible date", command=getCalendar).pack(pady=20)
    top.mainloop()