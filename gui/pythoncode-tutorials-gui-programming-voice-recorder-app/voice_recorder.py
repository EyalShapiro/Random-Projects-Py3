from tkinter import FALSE, Canvas, PhotoImage, ttk
from tkinter.messagebox import showinfo, showerror, askokcancel
from tkinter.tix import Tk
import sounddevice
from scipy.io.wavfile import write
import threading
from datetime import datetime
import time
import os

IMG_RECORDER = "recorder.png"
FILE_WAV = "recording.wav"


class VoiceRecorderApp:
    def __init__(self):
        self.window = Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.close_window)
        self.window.title("Voice Recorder")
        self.window.geometry("500x450+440+180")
        self.window.resizable(height=FALSE, width=FALSE)
        self.setup_styles()
        self.setup_canvas()
        self.setup_widgets()
        self.run()

    def run(self):
        self.window.mainloop()

    def close_window(self):
        if askokcancel(
            title="Close Voice Recorder",
            message="Are you sure you want to close the Voice Recorder?",
        ):
            self.window.destroy()

    def setup_styles(self):
        self.label_style = ttk.Style()
        self.label_style.configure("TLabel", foreground="#000000", font=("OCR A Extended", 15))
        self.entry_style = ttk.Style()
        self.entry_style.configure("TEntry", font=("Dotum", 15))
        self.button_style = ttk.Style()
        self.button_style.configure("TButton", foreground="red", font="DotumChe")

    def setup_canvas(self):
        self.canvas = Canvas(self.window, width=500, height=400)
        self.canvas.pack()
        self.logo = PhotoImage(file=IMG_RECORDER).subsample(2, 2)
        self.canvas.create_image(240, 135, image=self.logo)

    def setup_widgets(self):
        self.duration_label = ttk.Label(self.window, text="Enter Recording Duration in Sec(int):", style="TLabel")
        self.duration_entry = ttk.Entry(self.window, width=76, style="TEntry")
        self.canvas.create_window(240, 300, window=self.duration_label)
        self.canvas.create_window(250, 325, window=self.duration_entry)
        self.progress_label = ttk.Label(self.window, text="")
        self.record_button = ttk.Button(self.window, text="Record", style="TButton", command=self.recording_thread)
        self.canvas.create_window(242, 365, window=self.progress_label)
        self.canvas.create_window(240, 410, window=self.record_button)

    def record_voice(self):
        try:
            freq = 44100
            duration = int(self.duration_entry.get())
            recording = sounddevice.rec(duration * freq, samplerate=freq, channels=2)
            counter = 0
            while counter < duration:
                self.window.update()
                time.sleep(1)
                counter += 1
                self.progress_label.config(text=str(counter))
            sounddevice.wait()
            write(FILE_WAV, freq, recording)
            for file in os.listdir():
                if file == FILE_WAV:
                    base, ext = os.path.splitext(file)
                    current_time = datetime.now()
                    new_name = (
                        "recording-"
                        + str(current_time.hour)
                        + "."
                        + str(current_time.minute)
                        + "."
                        + str(current_time.second)
                        + ext
                    )
                    os.rename(file, new_name)
            showinfo("Recording complete", "Your recording is complete")
        except Exception as err:
            print("Error:", err)
            showerror(
                title="Error",
                message="An error occurred"
                "\nThe following could "
                "be the causes:\n->Bad duration value\n->An empty entry field\n"
                "Do not leave the entry empty and make sure to enter a valid duration value",
            )

    def recording_thread(self):
        t1 = threading.Thread(target=self.record_voice)
        t1.start()


if __name__ == "__main__":
    app = VoiceRecorderApp()
    app.run()
