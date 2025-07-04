import os
import ctypes
import pathlib
from tkinter import Tk, Toplevel, Listbox, StringVar, Entry, Button, Label, Menu, END


class SimpleExplorer:
    def __init__(self):
        # DPI awareness for sharper UI
        ctypes.windll.shcore.SetProcessDpiAwareness(True)

        self.root = Tk()
        self.root.title("Simple Explorer")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        # State
        self.currentPath = StringVar(self.root, name="currentPath", value=pathlib.Path.cwd())
        self.newFileName = StringVar(self.root, "new.txt", "new_name")
        self.currentPath.trace("w", self.pathChange)

        # GUI Elements
        self.setup_widgets()

        # Initialize with current path
        self.pathChange()

    def setup_widgets(self):
        Button(self.root, text="Folder Up", command=self.goBack).grid(sticky="NSEW", column=0, row=0)
        self.root.bind("<Alt-Up>", self.goBack)

        Entry(self.root, textvariable=self.currentPath).grid(sticky="NSEW", column=1, row=0, ipady=10, ipadx=10)

        self.list = Listbox(self.root)
        self.list.grid(sticky="NSEW", column=1, row=1, ipady=10, ipadx=10)
        self.list.bind("<Double-1>", self.changePathByClick)
        self.list.bind("<Return>", self.changePathByClick)

        menubar = Menu(self.root)
        menubar.add_command(label="Add File or Folder", command=self.open_popup)
        menubar.add_command(label="Quit", command=self.root.quit)
        self.root.config(menu=menubar)

    def pathChange(self, *event):
        try:
            directory = os.listdir(self.currentPath.get())
            self.list.delete(0, END)
            for file in directory:
                self.list.insert(0, file)
        except Exception as e:
            print(f"Error reading directory: {e}")

    def changePathByClick(self, event=None):
        try:
            picked = self.list.get(self.list.curselection()[0])
            path = os.path.join(self.currentPath.get(), picked)
            if os.path.isfile(path):
                print("Opening:", path)
                os.startfile(path)
            else:
                self.currentPath.set(path)
        except Exception as e:
            print(f"Error opening item: {e}")

    def goBack(self, event=None):
        newPath = pathlib.Path(self.currentPath.get()).parent
        self.currentPath.set(str(newPath))
        print("Going Back")

    def open_popup(self):
        self.top = Toplevel(self.root)
        self.top.geometry("250x150")
        self.top.resizable(False, False)
        self.top.title("Child Window")
        self.top.columnconfigure(0, weight=1)

        Label(self.top, text="Enter File or Folder name").grid()
        Entry(self.top, textvariable=self.newFileName).grid(column=0, pady=10, sticky="NSEW")
        Button(self.top, text="Create", command=self.newFileOrFolder).grid(pady=10, sticky="NSEW")

    def newFileOrFolder(self):
        name = self.newFileName.get()
        path = os.path.join(self.currentPath.get(), name)
        try:
            if "." in name:
                open(path, "w").close()
            else:
                os.mkdir(path)
            print(f"Created: {path}")
        except Exception as e:
            print(f"Error creating file/folder: {e}")
        finally:
            self.top.destroy()
            self.pathChange()

    def run(self):
        self.root.mainloop()


# Run the app
if __name__ == "__main__":
    app = SimpleExplorer()
    app.run()
