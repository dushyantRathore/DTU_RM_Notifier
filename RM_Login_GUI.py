from Tkinter import *
from RM_scraper import get_data
import pickle


# Initialisation Function


class initialise():

    def __init__(self):
        self.root = Tk()
        self.root.title("DTU Resume Manager Notifier")
        self.mainframe = Frame(self.root, padx=10, pady=10)
        self.label1 = Label(self.mainframe, text="Enter your username : ")
        self.label1.config(font=("Arial", 18))
        self.entry1 = Entry(self.mainframe, width=25)
        self.entry1.config(font=("Arial", 18))
        self.label2 = Label(self.mainframe, text="Enter your password : ")
        self.label2.config(font=("Arial", 18))
        self.entry2 = Entry(self.mainframe, width=25, show = "*")
        self.entry2.config(font=("Arial", 18))

        self.button1 = Button(self.mainframe, text="Login", command=self.login) # Associate the function to be called on clicking the login button
        self.button1.config(font=("Arial", 18))

        # Grid Packing

        self.label1.grid(row=0, sticky=E)
        self.entry1.grid(row=0, column=1)
        self.label2.grid(row=1, sticky=E)
        self.entry2.grid(row=1,column=1)
        self.button1.grid(row=2,column=0,columnspan=2)

        self.mainframe.pack()

        self.root.mainloop()

    def login(self):

        username = self.entry1.get()    # Get the username
        password = self.entry2.get()    # Get the password

        fileobject1 = open('username.txt', 'w')
        pickle.dump(username, fileobject1)

        fileobject2 = open('password.txt', 'w')
        pickle.dump(password,fileobject2)

if __name__ == "__main__":
     initialise()