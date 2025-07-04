import tkinter as tk


class BaseUI:
    """Base class for UI handling common theme and utility methods."""

    font = "Arial"

    THEME = {
        "bg_color": "#2E2E2E",
        "fg_color": "#00FFC3",
        "button_bg": "#4A4A4A",
        "button_fg": "#00CED1",
        "font": (font, 16, "bold"),
        "font_time": (font, 20, "bold"),
        "button_font": (font, 16, "bold"),
        "padding": 15,
        "button_width": 10,
        "messagebox_bg": "#4A4A4A",
        "messagebox_fg": "#00FFC3",
    }
    ONE_SEC = 1000

    def show_custom_messagebox(self, parent, title, message, msg_type="info"):
        """Show a custom styled messagebox."""
        dialog = tk.Toplevel(parent)
        dialog.transient(parent)
        dialog.title(title)
        dialog.configure(bg=self.THEME["bg_color"])
        dialog.resizable(False, False)
        dialog.geometry("300x200")

        # Center the dialog relative to parent
        dialog.update_idletasks()
        x = parent.winfo_rootx() + (parent.winfo_width() - 300) // 2
        y = parent.winfo_rooty() + (parent.winfo_height() - 150) // 2
        dialog.geometry(f"+{x}+{y}")

        # Message label
        label = tk.Label(
            dialog,
            text=message,
            fg=self.THEME["fg_color"],
            bg=self.THEME["bg_color"],
            font=self.THEME["font"],
            wraplength=280,
            pady=10,
            justify="center",
        )
        label.pack(expand=True)

        # OK button
        ok_btn = tk.Button(
            dialog,
            text="OK",
            fg=self.THEME["button_fg"],
            bg=self.THEME["button_bg"],
            font=self.THEME["button_font"],
            width=self.THEME["button_width"],
            command=dialog.destroy,
        )
        ok_btn.pack(pady=10)

        dialog.grab_set()
        parent.wait_window(dialog)


class BaseUIMode(BaseUI):
    """Base class for Timer and Stopwatch modes handling common UI and logic."""

    def __init__(self, parent=None):
        BaseUI.__init__(self)
        self.parent = parent if parent else tk.Tk()

        if parent is None:
            self.parent.title(self.__class__.__name__)
            self.parent.configure(bg=self.THEME["bg_color"])
            self.parent.minsize(width=400, height=250)
            self.parent.geometry("500x300")
            self.parent.resizable(True, True)
            self.parent.grid_columnconfigure(0, weight=1)
            self.parent.grid_rowconfigure(0, weight=1)
            self.parent.grid_rowconfigure(1, weight=1)
            self.parent.grid_rowconfigure(2, weight=1)

        self.counter = 0
        self.running = False

        # Back button (top-left, with arrow)
        if parent is not None:
            self.back_btn = tk.Button(
                self.parent,
                text="← Back",
                fg=self.THEME["button_fg"],
                bg=self.THEME["button_bg"],
                font=self.THEME["button_font"],
                width=self.THEME["button_width"],
                command=self.parent.show_home_page,
            )
            self.back_btn.grid(row=0, column=0, sticky="nw", padx=5, pady=5)

        # Create and configure frame for buttons
        self.frame_element = tk.Frame(self.parent, bg=self.THEME["bg_color"])
        self.frame_element.grid(row=2, column=0, pady=self.THEME["padding"], sticky="ew")

        # Configure grid for buttons
        self.frame_element.grid_columnconfigure(0, weight=1)
        self.frame_element.grid_columnconfigure(1, weight=1)
        self.frame_element.grid_columnconfigure(2, weight=1)

        # Create label for time display
        self.label = tk.Label(
            self.parent,
            fg=self.THEME["fg_color"],
            bg=self.THEME["bg_color"],
            font=self.THEME["font_time"],
            pady=self.THEME["padding"],
            justify="center",
        )
        self.label.grid(row=1, column=0, sticky="nsew", padx=self.THEME["padding"])

        # Create common buttons
        self.start_btn = tk.Button(
            self.frame_element,
            text="Start",
            fg=self.THEME["button_fg"],
            bg=self.THEME["button_bg"],
            font=self.THEME["button_font"],
            width=self.THEME["button_width"],
            command=self.start,
        )
        self.start_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.reset_btn = tk.Button(
            self.frame_element,
            text="Reset",
            fg=self.THEME["button_fg"],
            bg=self.THEME["button_bg"],
            font=self.THEME["button_font"],
            width=self.THEME["button_width"],
            state="disabled",
            command=self.reset,
        )
        self.reset_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.stop_btn = tk.Button(
            self.frame_element,
            text="Stop",
            fg=self.THEME["button_fg"],
            bg=self.THEME["button_bg"],
            font=self.THEME["button_font"],
            width=self.THEME["button_width"],
            state="disabled",
            command=self.stop,
        )
        self.stop_btn.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # Bind keyboard events
        self.setup_keyboard_events()

    def counter_label(self):
        """Abstract method to be implemented by subclasses."""
        raise NotImplementedError

    def compile_time(self):
        """Abstract method to be implemented by subclasses."""
        raise NotImplementedError

    def start(self):
        """Abstract method to be implemented by subclasses."""
        raise NotImplementedError

    def reset(self):
        """Abstract method to be implemented by subclasses."""
        raise NotImplementedError

    def stop(self):
        """Stop the mode."""
        self.start_btn["state"] = "normal"
        self.stop_btn["state"] = "disabled"
        self.reset_btn["state"] = "normal"
        self.running = False

    def handle_key(self, action, button=None):
        """Generic key handler to avoid code duplication and respect button state."""
        if button is None or button["state"] == "normal":
            print(f"Shortcut triggered: {action.__name__}")
            action()

    def setup_keyboard_events(self):
        """Set up keyboard event bindings using Tkinter's event system."""
        print(
            "Keyboard shortcuts enabled: Ctrl+T (Start), Ctrl+E (Stop), Ctrl+R (Reset), Ctrl+Q (Quit)"
            + (", Ctrl+B (Back)" if hasattr(self, "back_btn") else "")
        )
        self.parent.bind("<Control-t>", lambda e: self.handle_key(self.start, self.start_btn))
        self.parent.bind("<Control-e>", lambda e: self.handle_key(self.stop, self.stop_btn))
        self.parent.bind("<Control-r>", lambda e: self.handle_key(self.reset, self.reset_btn))
        self.parent.bind("<Control-q>", lambda e: self.handle_key(self.parent.destroy))
        if hasattr(self, "back_btn"):
            self.parent.bind("<Control-b>", lambda e: self.handle_key(self.parent.show_home_page, self.back_btn))

    def run(self):
        """Start the main application loop for standalone mode."""
        self.parent.mainloop()
