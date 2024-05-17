from tkinter import Button, Checkbutton, Label, Tk, IntVar

root = Tk()
place_x = 20
place_y = 0
data = {}  # Dictionary to store the selected languages


def update_data(language, var):
    if var.get() == 1:  # If the checkbox is checked
        data[language] = True
    else:
        data.pop(language, None)  # Remove the language from the dictionary if unchecked


def print_selected_languages():
    """return all the selected programming languages."""
    selected = list(data.keys())
    print("Selected languages:", selected)

    return selected


def main():
    global root, place_x, place_y

    Label(root, text="Select Programming language of your choice").place(
        x=place_x, y=place_y
    )

    languages = ["C", "C++", "C#", "Python", "Java"]
    vars_list = []

    for language in languages:
        var = IntVar()
        Checkbutton(
            root,
            text=language,
            takefocus=0,
            variable=var,
            command=lambda lang=language, v=var: update_data(lang, v),
        ).place(x=place_x + 5, y=place_y + 25)
        vars_list.append(var)
        place_y += 25

    print_button = Button(
        root, text="Print Selected Languages", command=print_selected_languages
    )
    print_button.place(x=20, y=place_y + 25)

    root.mainloop()


if __name__ == "__main__":
    main()
