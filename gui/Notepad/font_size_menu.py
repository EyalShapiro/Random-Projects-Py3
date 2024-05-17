from tkinter import Menu


class FontSizeMenu:
    def __init__(self, root, text_area):
        self.root = root
        self.text_area = text_area
        self.font_size = 12
        self.font_size_menu = Menu(self.root, tearoff=0)

        self.font_size_menu.add_command(label="+", command=self.increase_font_size)
        self.font_size_menu.add_command(label="-", command=self.decrease_font_size)

    def get_menu(self):
        return self.font_size_menu

    def increase_font_size(self):
        self.font_size += 1
        self.update_font_size()

    def decrease_font_size(self):
        if self.font_size > 1:
            self.font_size -= 1
            self.update_font_size()

    def update_font_size(self):
        self.text_area.config(font=("Helvetica", self.font_size))
