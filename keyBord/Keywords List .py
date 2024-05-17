import sys
import tkinter as tk
import keyword
import tkinter
from tkinter.constants import N
kl = keyword.kwlist

# creating window
t = tk.Tk()

# setting attribute
t.attributes('-fullscreen', True)
# creating text label to display on window screen


label = tk.Label(t, text='null',  font="Arial  10 bold")


def print_keywords(listd):
    t = ''
    for i in listd:
        t += i+'\n'
    print(t)
    label['text'] = t


def main():
    # printing all keywords at once using "k.w list()"
    print("The list of keywords is : ")
    print(kl)
    print_keywords(kl)
    quit = tk.Button(t, text='quit', width=25, command=sys.exit)
    label.pack()
    quit.pack()
    t.mainloop()

123
if __name__ == '__main__':
    main()
