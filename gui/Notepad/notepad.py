import tkinter as tk
from tkinter import Text, Scrollbar
from editor_menu import EditorMenu
from font_size_menu import FontSizeMenu


class Notepad:
    def __init__(self, **kwargs):
        self.root = tk.Tk()
        self.this_width = self.root.winfo_screenwidth()
        self.this_height = (
            self.root.winfo_screenheight() - 50
        )  # Adjust for the menu bar height
        self.this_text_area = Text(self.root, font=("Helvetica", 12))
        self.this_scroll_bar = Scrollbar(self.this_text_area)
        self.file = None

        try:
            self.root.wm_iconbitmap("Notepad.ico")
        except Exception as err:
            print(err)

        self.root.title(string="Untitled - Notepad")
        self.root.geometry(newGeometry=f"{self.this_width}x{self.this_height}")
        self.root.grid_rowconfigure(index=1, weight=1)  # Expand row 1
        self.root.grid_columnconfigure(index=0, weight=1)  # Expand column 0

        # Create and display the EditorMenu within the root frame
        self.editor_menu = EditorMenu(
            root=self.root,  # Pass the root window here
            text_area=self.this_text_area,
        )
        self.editor_menu.setup_editor()
        # Create and display the FontSizeMenu within the root frame
        self.font_size_menu = FontSizeMenu(
            root=self.root, text_area=self.this_text_area
        )
        self.font_size_menu = self.font_size_menu.get_menu()

        # Create toolbar for font size adjustment
        toolbar = tk.Frame(self.root, relief=tk.RAISED, bd=2)
        toolbar.grid(row=0, column=0, sticky=tk.W + tk.E)

        decrease_font_button = tk.Button(
            master=toolbar,
            text="-",
            command=self.decrease_font_size,
        )
        decrease_font_button.pack(side=tk.LEFT)

        self.font_size_label = tk.Label(master=toolbar, text=f"Font Size: {12}")
        self.font_size_label.pack(side=tk.LEFT, padx=5)

        increase_font_button = tk.Button(
            master=toolbar,
            text="+",
            command=self.increase_font_size,
        )
        increase_font_button.pack(side=tk.LEFT)

        self.this_text_area.grid(row=1, column=0, sticky=tk.N + tk.E + tk.S + tk.W)

    def increase_font_size(self):
        font_size = int(self.font_size_label["text"].split(": ")[-1]) + 1
        self.font_size_label.config(text=f"Font Size: {font_size}")
        self.this_text_area.config(font=("Helvetica", font_size))

    def decrease_font_size(self):
        font_size = int(self.font_size_label["text"].split(": ")[-1]) - 1
        if font_size > 0:
            self.font_size_label.config(text=f"Font Size: {font_size}")
            self.this_text_area.config(font=("Helvetica", font_size))

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    notepad = Notepad()
    notepad.run()
