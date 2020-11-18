# This is a draft login page
from tkinter import *
import sys

# Sample user data
users = {"admin": "123456", "user1": "111111", "user2": "password"}


class LoginWindow(Frame):
    """
    A LoginWindow class.
    """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        """
        Initialize a window with relevant widgets.
        """
        # Set the title and
        self.master.title("GUI")

        # Create a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Create the file object and add it to the menu
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        # Create the edit object and add it to the menu
        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)

        # Create username and password entry boxes
        username_label = Label(self.master, text="Username: ").grid(row=0, column=0)
        self.username_entry = Entry(self.master)
        self.username_entry.grid(row=0, column=1)

        password_label = Label(self.master, text="Password: ").grid(row=1, column=0)
        self.password_entry = Entry(self.master)
        self.password_entry.grid(row=1, column=1)

        # Create submit button
        submit = Button(self.master, text="Submit", command=self.attempt_login)
        submit.grid(row=2, column=1, columnspan=2)

    def attempt_login(self):
        """
        Check the user's entered username and password against the stored data and login if correct.
        """
        username = self.username_entry.get()
        password = self.password_entry.get()
        if users[username] == password:
            print("Correct login information!")
        else:
            print("Incorrect login information!")

    @staticmethod
    def client_exit():
        """
        Exit the application.
        """
        sys.exit()


# Using the class defined above, start the application
root = Tk()
root.geometry("300x200")
app = LoginWindow(root)
root.mainloop()
