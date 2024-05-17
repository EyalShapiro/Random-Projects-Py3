from tkinter import *
import time
import sys
import keyboard
'''
שעון עצר
Timer
'''
# ------------------------------------------------קבועים------------------------------------------------------------
_author_ = 'Eyal'

root = Tk()
counter = 0
running = False


f = Frame()
# תקסט ששעון לא פועל והזמן בשעון 0
label = Label(root, text="-=- Start='ctrl + t' -=- \n -=- Stop='ctrl + e' -=-\n -=- Reset='ctrl + r' -=-)",
              fg="green", font="Arial  10 bold")


# לחיצה כפתור מתחילה את הזמן בשעון
start = Button(f, text='Start', fg="dark cyan",
               state='normal', command=lambda: Start(label))
# לחיצה כפתור מהפסת את הזמן בשעון
reset = Button(f, text='Reset', fg="dark cyan",
                       state='disabled', command=lambda: Reset(label))
# לחיצה כפתור מהפסיקה את הזמן בשעון
stop = Button(f, text='Stop ', fg="dark cyan",
                      state='disabled', command=lambda: Stop())


# -------------------------------------------------------------------------------------------------------------------


def counter_label(label):

    def count():  # סופר זמן
        if running:
            global counter
            counter += 1
            label.config(text=str(Compile_Time()))
            label.after(1000, count)
    count()


def Compile_Time():  # שינוי הזמן שחלף משניות לשעות, דקות, שניות ומילי-שניות
    global counter
    sec = counter
    ty_res = time.gmtime(sec)
    res = time.strftime("%H:%M:%S", ty_res)
    return res


def Start(label):  # התחלה של שעון העצר
    """
    Start: button or keyboard='ctrl + t'
    """

    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


def Reset(label):  # איפוס שעון העצר
    """
    Reset: button or keyboard='ctrl + r'
    """
    global counter
    counter = 0
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = "Start='ctrl + t'\n Stop='ctrl + e'\n Reset='ctrl + r'"
    else:
        label['text'] = 'Starting...'


def Stop():  # עצירה של שעון העצר
    """
    Stop: button or keyboard='ctrl + e'
    """

    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False


def Key():
    """
    Start='ctrl + t'
    Reset='ctrl + r'
    Stop='ctrl + e'
    Quit ='ctrl + q'

    """
    print("Start='ctrl + t',Reset='ctrl + r',Stop='ctrl + e',Quit='ctrl + q'")
    global start, stop, reset, label

    if keyboard.is_pressed('ctrl + t'):
        print('Start')
        start.keys
    if keyboard.is_pressed('ctrl + r'):
        print('Reset')
        Reset(label)
    if keyboard.is_pressed('ctrl + e'):
        print('Stop')
        Stop()
    # quit 'לאוסיף לחצן 'ctrl + q'
    if keyboard.is_pressed('ctrl + q'):
        sys.exit()  # סיום קוד
    else:
        pass


def main():
    Key()
    print("Start: She clicked button or keyboard='ctrl + t'"
          + "\nReset: She clicked button or keyboard='ctrl + r'"
          + "\n Stop: She clicked button or keyboard='ctrl + e'")

    root.title("Time")
    root.minsize(width=150, height=50)
    label.pack()

    f.pack(anchor='center', pady=0)
    start.pack(side="left")
    stop.pack(side="left")
    reset.pack(side="left")
    root.mainloop()


if __name__ == '__main__':
    main()
