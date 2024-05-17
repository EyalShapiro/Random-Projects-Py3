from tkinter import *
import sys
counter = 0


def counter_label(label):
    counter = 0

    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()


def main():
    pass #בעיה שקוד כאן
if __name__ == '__main__':
    main()
    while True:
        root = Tk()
        label = Label(root, fg="dark green")
        label.pack()
        counter_label(label)
        quit = Button(root, text='quit', fg='gold4',
                      width=25, command=sys.exit)
        quit.pack()
        root.mainloop()
