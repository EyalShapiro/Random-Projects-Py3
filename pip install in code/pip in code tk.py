from tkinter import END, Button, Tk, Label, Text
import sys
import keyboard
import pip

_author_ = "Eyal"

root = Tk()
root.geometry("450x200")
root.title("pip install")

text = Label(root, fg="gold4", height=2, width=16)
input_text = Text(root, fg="gold4", height=2, width=24)
Output = Text(root, fg="gold4", height=4, width=24)


def press():
    """Paste function"""
    keyboard.send("ctrl+v")


def pip_install(package_name):
    """
    pip install a Python package
    """
    help_str = "pip install"
    if help_str == package_name[: len(help_str)]:
        package_name = package_name[len(help_str) :]

    if hasattr(pip, "main"):
        pip.main(["install", package_name])
    else:
        pip._internal.main(["install", package_name])


def take_input():
    name_package = input_text.get("2.4", "end-1c")
    print(name_package)
    pip_install(name_package)
    Output.insert(END, "Install the Package")


def main():
    pr = Label(text="Enter name for Python package\n ↓⇊↓ ")
    Display = Button(root, height=2, width=5, text="sand", command=lambda: take_input())
    v = Button(root, text="contrl v", width=6, command=lambda: press)
    pr.pack()
    input_text.pack()
    v.pack(side="right")

    Display.pack(side="left")
    Output.pack()
    quit_button = Button(root, text="quit", fg="gold4", width=25, command=sys.exit)
    quit_button.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
