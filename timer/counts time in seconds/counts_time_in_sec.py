from tkinter import Tk, Label, Button

"""A simple timer that counts time in seconds.
This code uses the Tkinter library to create a GUI"""
# ------------------------------------------------constant------------------------------------------------------------

root = Tk()
root.title("Timer")
sec = 0
time = Label(root, fg="green")
# -------------------------------------------------------------------------------------------------------------------


def tick():
    global sec
    sec += 1
    time["text"] = sec
    # Take advantage of the after method of the Label
    time.after(1000, tick)


def main():
    time.pack()
    Button(root, fg="blue", text="Start", command=tick).pack()
    root.mainloop()


if __name__ == "__main__":
    main()
