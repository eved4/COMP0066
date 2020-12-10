import pandas as pd
import datetime


class Calendar:

    def __init__(self, start='2020-12-01', end='2020-12-31', start_hour=9, end_hour=18):
        # Create initial table with all dates between the specified dates, in half-hour increments
        self.schedule = pd.DataFrame({"Date": pd.date_range(start, end, freq='0.5H')})

        # Split into date and time
        dates, times = zip(*[(d.date(), d.time()) for d in self.schedule['Date']])
        self.schedule = self.schedule.assign(Date=dates, Time=times)

        # Add columns for appointments and patient, initially empty
        self.schedule['Appointment'] = 0
        self.schedule['Patient username'] = ""
        self.schedule['Patient name'] = ""

        # Drop non-working hours
        self.schedule = self.schedule[
            (self.schedule['Time'] >= datetime.time(start_hour, 0))
            & (self.schedule['Time'] < datetime.time(end_hour, 0))]
        self.schedule.reset_index(inplace=True, drop=True)

    def add_entry(self, date, time, patient_username, patient_name):
        self.schedule.loc[(self.schedule['Date'] == date) & (self.schedule['Time'] == time),
                          ['Appointment']] = 1
        self.schedule.loc[(self.schedule['Date'] == date) & (self.schedule['Time'] == time),
                          ['Patient username']] = patient_username
        self.schedule.loc[(self.schedule['Date'] == date) & (self.schedule['Time'] == time),
                          ['Patient name']] = patient_name


    """
    def update_entry(self, date_time, entry_title, patient_email=None, entry_type=None):
        self.schedule[str(date_time)] = [entry_title, patient_email, entry_type]
    """

    def remove_entry(self, date, time):
        self.schedule.loc[(self.schedule['Date'] == date) & (self.schedule['Time'] == time), ['Appointment']] = 0
        self.schedule.loc[(self.schedule['Date'] == date) & (self.schedule['Time'] == time), ['Patient username']] = ""
        self.schedule.loc[(self.schedule['Date'] == date) & (self.schedule['Time'] == time), ['Patient name']] = ""


datetime.date(2020, 12, 1)