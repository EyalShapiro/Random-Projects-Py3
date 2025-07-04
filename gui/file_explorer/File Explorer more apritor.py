import os
import shutil
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import (
    StringVar,
    Toplevel,
    Frame,
    Label,
    Button,
    Entry,
    Listbox,
    Scrollbar,
    END,
    VERTICAL,
    RIGHT,
    Y,
    TRUE,
)


def open_a_file():
    files = fd.askopenfilename(title="Select a file of any type", filetypes=[("All files", "*.*")])
    os.startfile(os.path.abspath(files))


def copy_a_file():
    copythefile = fd.askopenfilename(title="Select a file to copy", filetypes=[("All files", "*.*")])
    dir_to_paste = fd.askdirectory(title="Select the folder to paste the file")
    try:
        shutil.copy(copythefile, dir_to_paste)
        mb.showinfo(title="File copied!", message="The file has been copied to the destination.")
    except Exception as err:
        mb.showerror(title="Error!", message="File is unable to copy. Please try again!")
        print(err)


def delete_a_file():
    files = fd.askopenfilename(title="Choose a file to delete", filetypes=[("All files", "*.*")])
    os.remove(os.path.abspath(files))
    mb.showinfo(title="File deleted!", message="The selected file has been deleted.")


def rename_a_file():
    rename_win = Toplevel(win_root)
    rename_win.title("Rename File")
    rename_win.geometry("300x100+300+250")
    rename_win.resizable(0, 0)
    rename_win.configure(bg="#F6EAD7")

    rename_label = Label(
        rename_win,
        text="Enter the file name:",
        font=("Calibri", "8"),
        bg="white",
        fg="blue",
    )
    rename_label.pack(pady=4)
    rename_field = Entry(
        rename_win,
        width=26,
        textvariable=fileNameEntered,
        relief=tk.GROOVE,
        font=("Calibri", "10"),
        bg="white",
        fg="blue",
    )
    rename_field.pack(pady=4, padx=4)

    submitButton = Button(
        rename_win,
        text="Submit",
        command=name_submit,
        width=14,
        relief=tk.GROOVE,
        font=("Calibri", "9"),
        bg="white",
        fg="blue",
        activebackground="#709218",
        activeforeground="#FFFFFF",
    )
    submitButton.pack(pady=2)


def show_file_path():
    files = fd.askopenfilename(title="Select the file to rename", filetypes=[("All files", "*.*")])
    return files


def name_submit():
    rename_name = fileNameEntered.get()
    fileNameEntered.set("")
    file_name = show_file_path()
    new_file_name = os.path.join(os.path.dirname(file_name), rename_name + os.path.splitext(file_name)[1])
    os.rename(file_name, new_file_name)
    mb.showinfo(title="File Renamed!", message="The selected file has been renamed.")


def open_a_folder():
    folder1 = fd.askdirectory(title="Select Folder to open")
    os.startfile(folder1)


def delete_a_folder():
    folder_to_delete = fd.askdirectory(title="Select Folder to delete")
    os.rmdir(folder_to_delete)
    mb.showinfo("Folder Deleted!", "The selected folder has been deleted!")


def move_a_folder():
    folder_to_move = fd.askdirectory(title="Select the folder you want to move")
    mb.showinfo(message="Folder has been selected to move. Now, select the desired destination.")
    des = fd.askdirectory(title="Destination")
    try:
        shutil.move(folder_to_move, des)
        mb.showinfo(
            "Folder moved!",
            "The selected folder has been moved to the desired Location",
        )
    except Exception as err:
        mb.showerror(
            "Error!",
            "The Folder cannot be moved. Make sure that the destination exists",
        )
        print(err)


def list_files_in_folder():
    i = 0
    folder1 = fd.askdirectory(title="Select the Folder")
    files = os.listdir(os.path.abspath(folder1))
    list_files_window = Toplevel(win_root)
    list_files_window.title(f"Files in {folder1}")
    list_files_window.geometry("300x500+300+200")
    list_files_window.resizable(0, 0)
    list_files_window.configure(bg="white")

    the_listbox = Listbox(
        list_files_window,
        selectbackground="#F24FBF",
        font=("Calibri", "10"),
        background="white",
    )
    the_listbox.place(relx=0, rely=0, relheight=1, relwidth=1)

    the_scrollbar = Scrollbar(the_listbox, orient=VERTICAL, command=the_listbox.yview)
    the_scrollbar.pack(side=RIGHT, fill=Y)
    the_listbox.config(yscrollcommand=the_scrollbar.set)

    while i < len(files):
        the_listbox.insert(END, "[" + str(i + 1) + "] " + files[i])
        i += 1
    the_listbox.insert(END, "")
    the_listbox.insert(END, "Total Files: " + str(len(files)))


if __name__ == "__main__":
    win_root = tk.Tk()
    win_root.title("File Explorer")
    win_root.geometry("400x600+650+250")
    win_root.resizable(0, 0)
    win_root.configure(bg="white")

    header_frame = Frame(win_root, bg="#D8E9E6")
    buttons_frame = Frame(win_root, bg="skyblue")

    header_frame.pack(fill="both")
    buttons_frame.pack(expand=TRUE, fill="both")

    header_label = Label(
        header_frame,
        text="File Explorer",
        font=("Calibri", "16"),
        bg="white",
        fg="blue",
    )

    header_label.pack(expand=TRUE, fill="both", pady=12)

    open_button = Button(
        buttons_frame,
        text="Open a File",
        font=("Calibri", "15"),
        width=20,
        bg="white",
        fg="blue",
        relief=tk.GROOVE,
        activebackground="blue",
        command=open_a_file,
    )

    rename_button = Button(
        buttons_frame,
        text="Rename a File",
        font=("Calibri", "15"),
        width=20,
        bg="white",
        fg="blue",
        relief=tk.GROOVE,
        activebackground="white",
        command=rename_a_file,
    )

    copy_button = Button(
        buttons_frame,
        text="Copy the File",
        font=("Calibri", "15"),
        width=20,
        bg="white",
        fg="blue",
        relief=tk.GROOVE,
        activebackground="blue",
        command=copy_a_file,
    )

    delete_button = Button(
        buttons_frame,
        text="Delete a File",
        font=("Calibri", "15"),
        width=20,
        bg="white",
        fg="blue",
        relief=tk.GROOVE,
        activebackground="white",
        command=delete_a_file,
    )

    open_folder_button = Button(
        buttons_frame,
        text="Open a Folder",
        font=("Calibri", "15"),
        width=20,
        bg="white",
        fg="Blue",
        relief=tk.GROOVE,
        activebackground="blue",
        command=open_a_folder,
    )

    delete_folder_button = Button(
        buttons_frame,
        text="Delete Folder",
        font=("Calibri", "15"),
        width=20,
        bg="white",
        fg="blue",
        relief=tk.GROOVE,
        activebackground="blue",
        command=delete_a_folder,
    )

    move_folder_button = Button(
        buttons_frame,
        text="Move the Folder",
        font=("Calibri", "15"),
        width=20,
        bg="white",
        fg="Blue",
        relief=tk.GROOVE,
        activebackground="Blue",
        command=move_a_folder,
    )

    list_button = Button(
        buttons_frame,
        text="List files in Folder",
        font=("Calibri", "15"),
        width=20,
        bg="white",
        fg="Blue",
        relief=tk.GROOVE,
        activebackground="Blue",
        command=list_files_in_folder,
    )

    fileNameEntered = StringVar()

    open_button.pack(pady=9)
    rename_button.pack(pady=9)
    copy_button.pack(pady=9)
    delete_button.pack(pady=9)
    move_folder_button.pack(pady=9)
    open_folder_button.pack(pady=9)
    delete_folder_button.pack(pady=9)
    list_button.pack(pady=10)
    win_root.mainloop()
