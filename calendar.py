class Calendar:
    """
    A class used to represent a Calendar. It can create, delete and update entries.
    The Calendar class is instantiated as an attribute of the GP and Nurse Classes.

    Attributes
    ----------
    schedule : dict
        A dictionairy containing all appointments of the GP.
        An appointment entry value is a list cointaining the title of the entry, 
        the patient participating in the appointment (optional) and the entry type (optional).
        The dictionairy key is the string format of a DateTime object.

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """
    def __init__(self, schedule={}):
        self.schedule = schedule

    def add_entry(self, date_time, entry_title, patient_email=None, entry_type=None):
        """
        Adds a new entry to the calendar.

        Arguments
        ----------
        date_time : str or DateTime
            The date and time of the appointment/calendar entry
        entry_title : str
            The title of the entry
        patient_email : str, optional
            The email address/username of the patient
        entry_type : str, optional
            The type of the entry (Out of office, Tentative, etc.)
        """
        self.schedule[str(date_time)] = [entry_title, patient_email, entry_type]

    def update_entry(self, date_time, entry_title, patient_email=None, entry_type=None):
        """
        Updates an entry in the calendar. 
        Same as add_entry, but separated for structural reasons.

        Arguments
        ----------
        date_time : str or DateTime
            The date and time of the appointment/calendar entry
        entry_title : str
            The title of the entry
        patient_email : str, optional
            The email address/username of the patient
        entry_type : str, optional
            The type of the entry (Out of office, Tentative, etc.)
        """
        self.schedule[str(date_time)] = [entry_title, patient_email, entry_type]

    def remove_entry(self, date_time):
        """
        Deletes an entry in the calendar. 

        Arguments
        ----------
        date_time : str or DateTime
            The date and time of the appointment/calendar entry
        """
        del self.schedule[str(date_time)]
        
        ######
        # In GP class
        #if appointment[2] != None:
            #patient = patient_list[appointment[2]]
        
            ## references patient method. Method needs some way of knowing if cancelled by gp to notify user
            ## maybe add notifications attribute to patient and gp
            #patient.canel_appointment(date_time, canceled_by_gp = True)
