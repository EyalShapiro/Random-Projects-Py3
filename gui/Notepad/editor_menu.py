import os
import tkinter as tk
from tkinter import colorchooser, filedialog, Menu
import webbrowser


class EditorMenu:
    def __init__(self, root, text_area):
        self.root = root
        self.text_area = text_area
        self.file_menu = Menu(self.root, tearoff=0)
        self.edit_menu = Menu(self.root, tearoff=0)
        self.help_menu = Menu(self.root, tearoff=0)
        self.file = None

        self.file_menu.add_command(label="New", command=self.__new_file)
        self.file_menu.add_command(label="Open", command=self.__open_file)
        self.file_menu.add_command(label="Save", command=self.__save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.__quit_application)

        self.edit_menu.add_command(label="Cut", command=self.__cut)
        self.edit_menu.add_command(label="Copy", command=self.__copy)
        self.edit_menu.add_command(label="Paste", command=self.__paste)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Change Text Color", command=self.__change_text_color)

        self.help_menu.add_command(label="About Notepad", command=self.__show_about)

    def setup_editor(self):
        self.main_menu = Menu(self.root)
        self.root.config(menu=self.main_menu)

        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.main_menu.add_command(label="Italic", command=self.__italic_text)
        self.main_menu.add_command(label="Bold", command=self.__bold_text)
        self.main_menu.add_command(label="Underline", command=self.__underline_text)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)

    def __quit_application(self):
        self.root.destroy()

    def __show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("About Notepad")
        about_window.configure(bg="skyblue")  # Set background color

        # Create a frame for padding and background color
        frame = tk.Frame(about_window, bg="#f0f0f0", padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        # Add a title label
        title_label = tk.Label(frame, text="About Notepad", font=("Arial", 14, "bold"), bg="#f0f0f0")
        title_label.pack(pady=(0, 10))

        # Add the name label
        label = tk.Label(frame, text="Eyal Shapiro", font=("Arial", 12), bg="#f0f0f0")
        label.pack(pady=(0, 10))

        # Add the link label
        link_label = tk.Label(
            frame,
            text="For more projects, visit my GitHub",
            fg="blue",
            underline=True,
            cursor="hand2",
            bg="#f0f0f0",
        )
        link_label.pack(pady=(0, 10))

        def open_github(event):
            webbrowser.open("https://github.com/EyalShapiro")

        link_label.bind("<Button-1>", open_github)

        # Add a close button
        close_button = tk.Button(
            frame,
            text="Close",
            command=about_window.destroy,
            bg="#e0e0e0",
            relief="flat",
        )
        close_button.pack(pady=(20, 0))

    def __open_file(self):
        self.file = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
        )
        if self.file:
            self.root.title(os.path.basename(self.file) + " - Notepad")
            self.text_area.delete(1.0, tk.END)
            with open(self.file, "r") as file:
                self.text_area.insert(1.0, file.read())

    def __new_file(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.text_area.delete(1.0, tk.END)

    def __save_file(self):
        if self.file is None:
            self.file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
            )
            if self.file:
                with open(self.file, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.root.title(os.path.basename(self.file) + " - Notepad")
        else:
            with open(self.file, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    def __getCurrent_tags(self):
        try:
            current_tags = self.text_area.tag_names("sel.first")
            if current_tags is None:
                return ("",)
            return current_tags
        except tk.TclError:
            return ("",)

    def __cut(self):
        self.text_area.event_generate("<<Cut>>")

    def __copy(self):
        self.text_area.event_generate("<<Copy>>")

    def __paste(self):
        self.text_area.event_generate("<<Paste>>")

    def __italic_text(self):
        current_tags = self.__getCurrent_tags()

        if "italic" in current_tags:
            self.text_area.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("italic", "sel.first", "sel.last")
            self.text_area.tag_configure("italic", font=("Helvetica", 12, "italic"))

    def __bold_text(self):
        current_tags = self.__getCurrent_tags()

        if "bold" in current_tags:
            self.text_area.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("bold", "sel.first", "sel.last")
            self.text_area.tag_configure("bold", font=("Helvetica", 12, "bold"))

    def __underline_text(self):
        current_tags = self.__getCurrent_tags()

        if "underline" in current_tags:
            self.text_area.tag_remove("underline", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("underline", "sel.first", "sel.last")
            self.text_area.tag_configure("underline", underline=True)

    def __change_text_color(self):
        color = colorchooser.askcolor(title="Choose Text Color")
        if color[1]:
            self.text_area.config(fg=color[1])
