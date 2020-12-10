from User import User
from datetime import datetime


class MedicalWorker(User):
    def __init__(self, userName, password, userType, title, firstName, lastName, birthDate, gender, telephone,
                 address, database):
        super(MedicalWorker, self).__init__(userName, password, userType, title, firstName, lastName, birthDate,
                                            gender, telephone, address)

        database["all_availability"][userName] = []
        self.appointment_finished = []
        self.appointment_confirmed = {}
        self.appointment_waiting = {}
        self.feedback = []

    def add_availability(self, new_availability, database):
        day_part, time_part = new_availability.split()
        from_time, to_time = time_part.split('-')
        availability_tuple = (datetime.strptime(day_part + " " + from_time, "%m/%d/%Y %H:%M"),
                              datetime.strptime(day_part + " " + to_time, "%m/%d/%Y %H:%M"))
        database["all_availability"][self.userName].append(availability_tuple)

    def confirm_appointment(self, appointmentID, database):
        # change status of confirmed appointment
        database["appointment"][appointmentID].status = "accepted"
        database["user_confirmed"][database["appointment"][appointmentID].patientUserName].appointment.append(appointmentID)

        affected_availability = database["appointment"][appointmentID].appointmentDateTimeTuple
        # change other appointments whose time is same as the confirmed one
        appointmentsID_at_same_time = self.appointment_waiting[affected_availability]
        for id in appointmentsID_at_same_time:
            if id != appointmentID:
                database["appointment"][id].status = "denied"
        # update appointment queue
        self.appointment_confirmed[affected_availability] = appointmentID
        self.appointment_waiting.pop(affected_availability)

    @staticmethod
    def print_availability(availability_datetime_tuple):
        from_time, to_time = availability_datetime_tuple
        print(datetime.strftime(from_time, "%m/%d/%Y %H:%M") + "-" + datetime.strftime(to_time, "%H:%M"))

    def display_appointment_waiting(self, database):
        mapping_id = []
        number = 1
        for avalability, waiting_queue in self.appointment_waiting.items():
            for appointmentID in waiting_queue:
                print(number, end=". ")
                number += 1
                appointment = database["appointment"][appointmentID]
                appointment.display_to_gp(database)
                mapping_id.append(appointmentID)
        return mapping_id

    def display_appointment_confirmed(self, database):
        mapping_id = []
        number = 1
        for avalability, confirmed_appointmentID in self.appointment_confirmed.items():
            print(number, end=". ")
            number += 1
            appointment = database["appointment"][confirmed_appointmentID]
            appointment.display_to_gp(database)
            mapping_id.append(confirmed_appointmentID)
        return mapping_id