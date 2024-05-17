import time
from tkinter import *
import _thread
import sys

_author_ = 'Eyal'


def Timer_now():
    while True:
        t = time.strftime('%I:%M:%S', time.localtime())
        time_label['text'] = t


def main():
    pass


if __name__ == '__main__':
    main()
    while True:
        root = Tk()
        root.geometry('200x100')
        time_label = Label(root, text='0:0:0', width=32)
        time_label.pack()
        quit = Button(root, text='quit', fg='gold4',
                      width=25, command=sys.exit)
        quit.pack()
        _thread.start_new_thread(Timer_now, ())
        root.mainloop()
