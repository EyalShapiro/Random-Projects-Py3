import tkinter as tk

import sys

if __name__ == "__main__":
    # creating window
    root = tk.Tk()
    filer_photo = r"./LPY.png"
    # Add image file
    bg = tk.PhotoImage(file=filer_photo)
    # setting attribute
    root.attributes("-fullscreen", True)
    root.title("full")

    # Show image using label
    tk.Label(root, image=bg).place(x=50, y=50)
    # creating text label to display on window screen
    label = tk.Label(root, text="Hello Tkinter!", font="arial 24 bold", bg="honeydew", fg="dark cyan")
    quit = tk.Button(
        root,
        text="quit",
        font="arial 24 bold",
        bg="honeydew",
        fg="dark cyan",
        command=sys.exit,
    )
    quit.pack()
    label.pack()
    root["bg"] = "green"

    root.mainloop()
