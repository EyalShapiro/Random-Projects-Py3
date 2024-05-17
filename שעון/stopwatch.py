from tkinter import *
import sys
import time
global count
count = 0


class stopwatch():
    def Reset(self):  # מרנן
        global count
        count = 1
        self.t.set('00:00:00')

    def Start(self):  # מתחילה
        global count
        count = 0
        self.timer()

    def Stop(self):  # עוצר
        global count
        count = 1

    def close(self):  # סוגר
        self.root.destroy()

    def Timer(self):
        global count
        if(count == 0):
            self.d = str(self.t.get())
            h, m, s = map(int, self.d.split(":"))
            h = int(h)
            m = int(m)
            s = int(s)
            if(s < 59):
                s += 1
            elif(s == 59):
                s = 0
                if(m < 59):
                    m += 1
                elif(m == 59):
                    m = 0
                    h += 1
            if(h < 10):
                h = str(0)+str(h)
            else:
                h = str(h)
            if(m < 10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s < 10):
                s = str(0)+str(s)
            else:
                s = str(s)
            self.d = h+":"+m+":"+s
            self.t.set(self.d)
            if(count == 0):
                self.root.after(10, self.Timer)

    def __init__(self):
        self.root = Tk()
        self.root.title("Stop Watch")
        self.root.geometry("250x150")
        self.timer = StringVar()
        self.timer.set("00:00:00")
        self.lb = Label(self.root, textvariable=self.timer,
                        font=("Times 40 bold"), fg="OrangeRed2", bg="black")
        self.start = Button(self.root, text="Start", command=self.Start, font=(
            "Times 12 bold"), bg='dark cyan')  # Start
        self.stop = Button(self.root, text="Stop", command=self.Stop, font=(
            "Times 12 bold"), bg='dark cyan')  # Stop
        self.reset = Button(self.root, text="Reset", command=self.Reset, font=(
            "Times 12 bold"), bg='dark cyan')  # Reset
        self.exit = Button(self.root, text="Exit", command=self.close, font=(
            "Times 12 bold"), bg='dark cyan')  # Exit
        self.lb.pack()
        self.start.pack(side="left")
        self.stop.pack(side="left")
        self.reset.pack(side="left")
        self.exit.pack()
        self.label = Label(self.root, text="", font=("Times 40 bold"))
        self.root.configure(bg='black')
        self.root.mainloop()


def main():
    a = stopwatch()


if __name__ == '__main__':
    main()
