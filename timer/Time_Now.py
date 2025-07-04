import time
from tkinter import Tk, Label, Button
from _thread import start_new_thread as start_thread
import sys


def create_my_windows():
    windows = Tk()
    windows.geometry("200x100")
    windows.title("time-now")
    return windows


def Timer_now(time_label: Label):
    while True:
        t = time.strftime("%I:%M:%S", time.localtime())
        time_label["text"] = t


def start():
    while True:
        root = create_my_windows()
        time_label = Label(root, text="0:0:0", width=32)
        time_label.pack()
        quit = Button(root, text="quit", fg="gold4", width=25, command=sys.exit)
        quit.pack()
        start_thread(Timer_now, (time_label,))
        root.mainloop()


def main():
    start()


if __name__ == "__main__":
    main()
