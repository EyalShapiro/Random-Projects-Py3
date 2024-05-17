import sqlite3

from tkinter import messagebox
import os
from tkinter import *
from Class_ContactManager import ContactManager


class Login:
    def __init__(self, root, login_user={"username": "", "password": ""}):
        # Initialize the class with the root window passed as an argument
        self.tk = root
        # Set the title of the root window
        self.tk.title("Contact Book Management System")
        self.tk.geometry("300x150")
        # Create StringVar variables to store the username and password
        self.username_inp = StringVar()
        self.password_inp = StringVar()
        self.login_user = login_user
        # ניתב מיקום קובץ לדוגמא "/home/User/Desktop/"
        path = os.path.split(os.path.abspath(__file__))[0]
        try:
            self.db_path = path + "\\DB\\" + self.username_inp + r".db"  # database קובץ

        except:
            self.db_path = path + "\\DB\\" + r"\ContactBook.db"  # database קובץ

        # Create a label and entry field for the username
        Label(self.tk, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        Entry(self.tk, textvariable=self.username_inp).grid(
            row=0, column=1, padx=10, pady=10
        )
        # Create a label and entry field for the password
        Label(self.tk, text="Password:").grid(row=1, column=0, padx=10, pady=10)
        Entry(self.tk, textvariable=self.password_inp, show="*").grid(
            row=1, column=1, padx=10, pady=10
        )
        # Create a login button that calls the login method when clicked
        Button(self.tk, text="Login", fg="dark blue", command=self.login).grid(
            columnspan=4, row=2, column=0, padx=0, pady=0
        )
        Button(master=self.tk, text="exit", fg="dark blue", command=root.destroy).grid(
            row=2, column=1, columnspan=1, padx=0, pady=0
        )

        return self.db_path

    def login(self):
        # Check if the entered username and password are correct
        # You can change the default username and passowrd here !
        if self.username_inp.get() == str(
            self.login_user["username"]
        ) and self.password_inp.get() == str(self.login_user["password"]):
            # If the login is successful, destroy the current window and open a new window
            global root
            root.destroy()
            root = Tk()  # גורת את משתנה ויוצר חדש

            ContactManager(path_book=self.db_path, root=root)
        else:
            # If the login is unsuccessful, show an error message
            messagebox.showerror("Error", "Invalid username or password")


def create_contact_table(db_path):
    """
    Create a contact table in a SQLite database.
    Parameters: - db_path: A string representing the filename of the contact book database.
    Returns:    - con: A SQLite database connection object.
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS contact (
            firstname VARCHAR(20),
            lastname VARCHAR(20),
            mobile VARCHAR(20) PRIMARY KEY,
            addr VARCHAR(20),
            pin VARCHAR(20)
        )
        """
    )
    return con


def start(login_user: dict):
    # Create a Tkinter root window
    root = Tk()
    # Create a Login object and pass the root window as an argument
    obj_log = Login(root, login_user)
    db_path = obj_log.db_path
    print(db_path)
    con = create_contact_table(db_path)
    return root, con


if __name__ == "__main__":
    # login_user = {"username": "al", "password": "123"}
    login_user = {"username": "", "password": ""}

    root = start(login_user)[0]
    # Start the main loop of the Tkinter program
    root.mainloop()


# if __name__ == "__main__":
#     Start()
