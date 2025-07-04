import tkinter as tk
import time

from ui import BaseUI, BaseUIMode


class App_Time(BaseUI, tk.Tk):
    """Main application class with home page for selecting Timer or Stopwatch."""

    __author__ = "Eyal"

    def __init__(self):
        tk.Tk.__init__(self)
        BaseUI.__init__(self)

        self.title("Timer & Stopwatch")
        self.configure(bg=self.THEME["bg_color"])
        self.minsize(width=400, height=250)
        self.geometry("500x300")
        self.resizable(True, True)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.show_home_page()

    def clear_window(self):
        """Clear all widgets from the window."""
        for widget in self.winfo_children():
            widget.destroy()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def show_home_page(self):
        """Display the home page with mode selection."""
        self.clear_window()

        label = tk.Label(
            self,
            text="Choose Mode",
            fg=self.THEME["fg_color"],
            bg=self.THEME["bg_color"],
            font=self.THEME["font"],
            pady=self.THEME["padding"],
        )
        label.grid(row=0, column=0, sticky="nsew", padx=self.THEME["padding"])

        frame = tk.Frame(self, bg=self.THEME["bg_color"])
        frame.grid(row=1, column=0, pady=self.THEME["padding"], sticky="ew")
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        timer_btn = tk.Button(
            frame,
            text="Timer",
            fg=self.THEME["button_fg"],
            bg=self.THEME["button_bg"],
            font=self.THEME["button_font"],
            width=self.THEME["button_width"],
            command=lambda: self.start_mode(TimerMode),
        )
        timer_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        stopwatch_btn = tk.Button(
            frame,
            text="Stopwatch",
            fg=self.THEME["button_fg"],
            bg=self.THEME["button_bg"],
            font=self.THEME["button_font"],
            width=self.THEME["button_width"],
            command=lambda: self.start_mode(StopwatchMode),
        )
        stopwatch_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    def start_mode(self, mode_class):
        """Start the specified mode."""
        self.clear_window()
        mode_class(self)

    def run(self):
        """Start the main application loop."""
        self.mainloop()


class TimerMode(BaseUIMode):
    """Timer mode that counts up."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.label.config(text="00:00:00")

    def counter_label(self):
        """Update the timer display."""

        def count():
            if self.running:
                self.counter += 1
                self.label.config(text=str(self.compile_time()))
                self.label.after(self.ONE_SEC, count)

        count()

    def compile_time(self):
        """Convert elapsed time from seconds to HH:MM:SS format."""
        sec = self.counter
        ty_res = time.gmtime(sec)
        res = time.strftime("%H:%M:%S", ty_res)
        return res

    def start(self):
        """Start the timer."""
        self.running = True
        self.counter_label()
        self.start_btn["state"] = "disabled"
        self.stop_btn["state"] = "normal"
        self.reset_btn["state"] = "normal"

    def reset(self):
        """Reset the timer."""
        self.counter = 0
        self.running = False
        self.reset_btn["state"] = "disabled"
        self.start_btn["state"] = "normal"
        self.stop_btn["state"] = "disabled"
        self.label["text"] = "00:00:00"


class StopwatchMode(BaseUIMode):
    """Stopwatch mode that counts down from user input."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.label.config(text="00:00:00")

        # Time entry (moved to row above buttons)
        self.time_entry = tk.Entry(
            self.parent, font=self.THEME["button_font"], width=self.THEME["button_width"], justify="center"
        )
        self.time_entry.grid(
            row=1,
            column=0,
            pady=8,
            sticky="n",
        )
        self.time_entry.insert(0, "00:00")
        self.time_entry.bind("<Return>", lambda event: self.start())  # Bind Enter key

        # Adjust frame row to be below entry
        self.frame_element.grid(row=2, column=0)

        # Shift buttons
        self.start_btn.grid(row=0, column=0)
        self.reset_btn.grid(row=0, column=1)
        self.stop_btn.grid(row=0, column=2)

    def compile_time(self):
        """Convert remaining seconds to HH:MM:SS format."""
        sec = max(0, self.counter)
        return self.compile_time_format(sec)

    def compile_time_format(self, sec):
        hours = sec // 3600
        minutes = (sec % 3600) // 60
        seconds = sec % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def validate_time(self):
        """Validate and convert HH:MM:SS or MM:SS input to seconds."""
        try:
            time_str = self.time_entry.get()
            if not time_str or type(time_str) is not str or len(time_str.strip()) == 0:
                raise ValueError("Input cannot be empty")
            time_str = str(time_str).strip()

            time_format = time_str.split(":")

            if len(time_format) == 1:
                hours, minutes = 0, 0
                seconds = int(time_format[0])
            elif len(time_format) == 2:
                hours = 0
                minutes, seconds = map(int, time_format)
            elif len(time_format) == 3:
                hours, minutes, seconds = map(int, time_format)
            else:
                raise ValueError("Invalid format")

            if hours >= 0 and minutes >= 0 and seconds >= 0:
                return hours * 3600 + minutes * 60 + seconds
            else:
                raise ValueError("Values must be non-negative")
        except (ValueError, AttributeError):
            self.show_custom_messagebox(self.parent, "Invalid Input", "Please enter time in HH:MM:SS or MM:SS format")
            return None

    def counter_label(self):
        """Update the stopwatch display."""

        def count():
            if self.running and self.counter > 0:
                self.counter -= 1
                self.label.config(text=str(self.compile_time()))
                self.parent.after(self.ONE_SEC, count)  # Use parent.after
            elif self.counter <= 0 and self.running:
                self.stop()
                self.label.config(text="Time's up!")
                self.show_custom_messagebox(self.parent, "Stopwatch", "Time's up!")

        count()

    def start(self):
        """Start the stopwatch."""
        seconds = self.validate_time()
        if seconds is None:
            return
        self.counter = seconds
        self.label.config(text=str(self.compile_time()))  # Update label immediately
        if self.counter > 0:
            self.running = True

            self.counter_label()
            self.start_btn["state"] = "disabled"
            self.stop_btn["state"] = "normal"
            self.reset_btn["state"] = "normal"
            self.time_entry["state"] = "disabled"
            self.time_entry.pack_forget()

    def reset(self):
        """Reset the stopwatch."""
        self.counter = 0
        self.running = False
        self.reset_btn["state"] = "disabled"
        self.start_btn["state"] = "normal"
        self.stop_btn["state"] = "disabled"
        self.time_entry["state"] = "normal"
        self.label["text"] = "00:00:00"


if __name__ == "__main__":
    # Example usage: can run either mode directly or through App_Time
    app = App_Time()
    # app = StopwatchMode()  # Uncomment to run StopwatchMode directly
    # app = TimerMode()      # Uncomment to run TimerMode directly
    app.run()
