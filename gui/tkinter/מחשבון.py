from tkinter import *


def buttonClick(numbers):
    global operator  # global expression variable
    operator = operator + str(numbers)
    text_Input.set(operator)


def buttonClearDisplay():
    global operator

    operator = ""
    text_Input.set("")


def buttonEqualsInput():

    try:
        global operator

        answer = str(eval(operator))
        text_Input.set(answer)

        # initializes the expression variable
        # to an empty string
        operator = ""

    except Exception as err:
        # if an error is generated then handle
        # using the except block
        text_Input.set("error")
        operator = ""


cal = Tk()  # instantiate
cal.title("Calculator")  # set title of GUI window
operator = ""

text_Input = StringVar()

textDisplay = Entry(
    cal,
    font=("Times New Roman", 20, "bold"),
    textvariable=text_Input,
    bd=30,
    insertwidth=4,
    bg="powder blue",
    justify="right",
).grid(columnspan=4)

# Row 1
button7 = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="7",
    command=lambda: buttonClick(7),
).grid(row=1, column=0)


button8 = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="8",
    command=lambda: buttonClick(8),
).grid(row=1, column=1)
button9 = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="9",
    command=lambda: buttonClick(9),
).grid(row=1, column=2)
Addition = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="+",
    command=lambda: buttonClick("+"),
).grid(row=1, column=3)

# ========================================================================================================================

# Row 2

button4 = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="4",
    command=lambda: buttonClick(4),
).grid(row=2, column=0)
button5 = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="5",
    command=lambda: buttonClick(5),
).grid(row=2, column=1)
button6 = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="6",
    command=lambda: buttonClick(6),
).grid(row=2, column=2)
Subtraction = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="-",
    command=lambda: buttonClick("-"),
).grid(row=2, column=3)

# ========================================================================================================================

# Row 3

button1 = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="1",
    command=lambda: buttonClick(1),
).grid(row=3, column=0)
button2 = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="2",
    command=lambda: buttonClick(2),
).grid(row=3, column=1)
button3 = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="3",
    command=lambda: buttonClick(3),
).grid(row=3, column=2)
Multiplication = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="*",
    command=lambda: buttonClick("*"),
).grid(row=3, column=3)

# ========================================================================================================================

# Row 4

button0 = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="0",
    command=lambda: buttonClick(0),
).grid(row=4, column=0)
buttonClear = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="CE",
    command=buttonClearDisplay,
).grid(row=4, column=1)
buttonEqual = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="=",
    command=buttonEqualsInput,
).grid(row=4, column=2)
Division = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text="/",
    command=lambda: buttonClick("/"),
).grid(row=4, column=3)

# ========================================================================================================================

# Row 5

Decimal = Button(
    cal,
    padx=16,
    pady=16,
    bd=8,
    fg="black",
    font=("arial", 20, "bold"),
    text=".",
    command=lambda: buttonClick("."),
).grid(row=5, column=0)
Dummy1 = Button(
    cal, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="PY"
).grid(row=5, column=1)
Dummy2 = Button(
    cal, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="TH"
).grid(row=5, column=2)
Dummy3 = Button(
    cal, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"), text="ON"
).grid(row=5, column=3)


def main():
    cal.mainloop()


if __name__ == "__main__":
    main()
