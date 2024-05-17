from tkinter import ttk, messagebox
from tkinter import *
import sqlite3


class ContactManager:
    def __init__(self, root, path_book):
        # Initialize the class with the root window passed as an argument
        self.root = root
        self.path_book = path_book
        # Set the title and size of the root window
        self.root.title("ContactBook Management")
        self.root.attributes("-fullscreen", True)
        # Create a label with the title text and style it
        title = Label(
            self.root,
            text="ContactBook Management",
            font=(
                "Comic Sans MS",
                20,
            ),
            bd=8,
            bg="black",
            fg="white",
        )
        title.pack(side=TOP, fill=X)
        # Create StringVar variables to store the contact details
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.mobile = StringVar()
        self.addr = StringVar()
        self.pin = StringVar()

        # Create a frame to hold the Contact details
        Detail_F = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Detail_F.place(x=10, y=120, width=350, height=260)

        # Create a label and entry field for the firstname
        lbl_name = Label(
            Detail_F,
            text="First Name",
            font=(
                "Comic Sans MS",
                12,
            ),
        )
        lbl_name.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(
            Detail_F,
            font=(
                "Comic Sans MS",
                10,
            ),
            bd=3,
            textvariable=self.firstname,
        )
        txt_name.grid(row=1, column=1, pady=10, sticky="w")

        # Create a label and entry field for the lastname
        lbl_mob = Label(
            Detail_F,
            text="Last Name",
            font=(
                "Comic Sans MS",
                12,
            ),
        )
        lbl_mob.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_mob = Entry(
            Detail_F,
            font=(
                "Comic Sans MS",
                10,
            ),
            bd=3,
            textvariable=self.lastname,
        )
        txt_mob.grid(row=2, column=1, pady=10, sticky="w")

        # Create a label and entry field for the Mobile number
        lbl_aa = Label(
            Detail_F,
            text="Mobile No.",
            font=(
                "Comic Sans MS",
                12,
            ),
        )
        lbl_aa.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_aa = Entry(
            Detail_F,
            font=(
                "Comic Sans MS",
                10,
            ),
            bd=3,
            textvariable=self.mobile,
        )
        txt_aa.grid(row=3, column=1, pady=10, sticky="w")

        # Create a label and entry field for the address
        lbl_add = Label(
            Detail_F,
            text="Address",
            font=(
                "Comic Sans MS",
                12,
            ),
        )
        lbl_add.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        txt_add = Entry(
            Detail_F,
            font=(
                "Comic Sans MS",
                10,
            ),
            bd=3,
            textvariable=self.addr,
        )
        txt_add.grid(row=4, column=1, pady=10, sticky="w")

        # Create a label and entry field for the pincode
        lbl_pin = Label(
            Detail_F,
            text="PinCode",
            font=(
                "Comic Sans MS",
                12,
            ),
        )
        lbl_pin.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_pin = Entry(
            Detail_F,
            font=(
                "Comic Sans MS",
                10,
            ),
            bd=3,
            textvariable=self.pin,
        )
        txt_pin.grid(row=5, column=1, pady=10, sticky="w")

        recordFrame = Frame(self.root, bd=5, relief=RIDGE)
        recordFrame.place(x=400, y=120, width=550, height=260)

        yscroll = Scrollbar(recordFrame, orient=VERTICAL)
        # Create a treeview to display the records
        self.contact_table = ttk.Treeview(
            recordFrame,
            columns=("firstname", "lastname", "mobile", "address", "pin"),
            yscrollcommand=yscroll.set,
        )
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.contact_table.yview)
        self.contact_table.heading("firstname", text="First Name")
        self.contact_table.heading("lastname", text="Last Name")
        self.contact_table.heading("mobile", text="Mobile No.")
        self.contact_table.heading("address", text="Address")
        self.contact_table.heading("pin", text="PinCode")

        self.contact_table["show"] = "headings"

        self.contact_table.column("firstname", width=100)
        self.contact_table.column("lastname", width=100)
        self.contact_table.column("mobile", width=100)
        self.contact_table.column("address", width=100)
        self.contact_table.column("pin", width=110)
        self.contact_table.pack(fill=BOTH, expand=1)
        self.fetch_data()
        self.contact_table.bind("<ButtonRelease-1>", self.get_cursor)

        btnFrame = Frame(self.root, bd=5, relief=RIDGE)
        btnFrame.place(x=250, y=400, width=650, height=80)

        # Create a button to calculate the Details
        Button(
            btnFrame,
            text="Add record",
            font="arial 12 bold",
            bg="black",
            fg="white",
            width=9,
            command=self.AddRecord,
        ).grid(row=0, column=0, padx=10, pady=10)
        # Create a button to update the Details
        Button(
            btnFrame,
            text="Update",
            font="arial 12 bold",
            bg="black",
            fg="white",
            width=9,
            command=self.update,
        ).grid(row=0, column=1, padx=8, pady=10)
        # Create a button to delete the entry
        Button(
            btnFrame,
            text="Delete",
            font="arial 12 bold",
            bg="black",
            fg="white",
            width=9,
            command=self.delete,
        ).grid(row=0, column=2, padx=8, pady=10)
        # Create a button to reset the fields

        Button(
            btnFrame,
            text="Reset",
            font="arial 12 bold",
            bg="black",
            fg="white",
            width=9,
            command=self.reset,
        ).grid(row=0, column=3, padx=8, pady=10)
        # Create a button to exit the clos

        Button(
            btnFrame,
            text="Close",
            font="arial 12 bold",
            fg="snow",
            bg="darkred",
            width=9,
            command=root.destroy,
        ).grid(row=0, column=4, padx=8, pady=10)

    def AddRecord(self):
        if (
            self.firstname.get() == ""
            or self.lastname.get() == ""
            or self.mobile.get() == ""
            or self.addr.get() == ""
            or self.pin.get() == ""
        ):
            messagebox.showerror("Error", "Please enter details ?")
        else:
            con = sqlite3.connect(self.path_book)
            cur = con.cursor()
            cur.execute("Select * from contact")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == self.mobile.get():
                    messagebox.showerror("Error", "Duplicates not allowed")
                    return
            cur.execute(
                "insert into contact values(?,?,?,?,?)",
                (
                    self.firstname.get(),
                    self.lastname.get(),
                    self.mobile.get(),
                    self.addr.get(),
                    self.pin.get(),
                ),
            )
            con.commit()
            self.fetch_data()
            con.close()

    def fetch_data(self):
        con = sqlite3.connect(self.path_book)
        cur = con.cursor()
        cur.execute("select firstname , lastname , mobile , addr , pin  from contact")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.contact_table.delete(*self.contact_table.get_children())
            for row in rows:
                self.contact_table.insert("", END, values=row)
        con.commit()
        con.close()

    def update(self):
        # Check if a record has been selected to update
        if self.mobile.get() == "":
            messagebox.showerror("Error", "Select a record to update !")
        else:
            # Connect to the database
            con = sqlite3.connect(self.path_book)
            cur = con.cursor()
            # Update the contact in the database using the current values of the input fields
            cur.execute(
                "update contact set firstname = ?, lastname = ?, mobile = ?, addr = ?, pin = ? where mobile = ?",
                (
                    self.firstname.get(),
                    self.lastname.get(),
                    self.mobile.get(),
                    self.addr.get(),
                    self.pin.get(),
                    self.mobile.get(),
                ),
            )
            # Show a success message and close the database connection
            messagebox.showinfo(
                "Info", f"Record {self.mobile.get()} Updated Successfully"
            )
            con.commit()
            con.close()
            # Refresh the data in the table and reset the input fields
            self.fetch_data()
            self.reset()

    def delete(self):
        # Check if the contact ID has been entered
        if self.mobile.get() == "":
            messagebox.showerror("Error", "Enter contact ID to delete the records")
        else:
            # Connect to the database
            con = sqlite3.connect(self.path_book)
            cur = con.cursor()
            # Delete the contact from the database using the current contact ID
            cur.execute("delete from contact where mobile = ?", (self.mobile.get(),))
            # Close the database connection
            con.commit()
            con.close()
            # Refresh the data in the table and reset the input fields
            self.fetch_data()
            self.reset()

    def reset(self):
        # Reset the values of the input fields
        self.firstname.set("")
        self.lastname.set("")
        self.mobile.set("")
        self.addr.set("")
        self.pin.set("")

    def get_cursor(self, ev):
        # Get the row that the cursor is currently on in the table
        cursor_row = self.contact_table.focus()
        # Get the content of that row
        content = self.contact_table.item(cursor_row)
        # Get the values of that row
        row = content["values"]
        # Set the input fields to the values of the selected row
        self.firstname.set(row[0])
        self.lastname.set(row[1])
        self.mobile.set(row[2])
        self.addr.set(row[3])
        self.pin.set(row[4])
