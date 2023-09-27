# Simple Calculator App
# This program creates a basic calculator GUI using Tkinter.
# Users can perform addition, subtraction, multiplication, and division.

import tkinter as tk

window = tk.Tk()
window.geometry("300x400")
window.title("Calculator")
window.resizable(False,False)

# Initializing a variable that will contain a combination of numbers and operators for the calculator to calculate.
calculation = ""

# Add number or operator to the calculation variable. This function is executed when a button of a number or an operator is clicked.
def add_symbol(symbol):
    global calculation
    calculation = calculation + str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Set the calculation variable to blank and delete text in text box.
def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

# Evaluate the operations from the input using the eval() function and output the result to the textbox. 
# Basic error handling in the except block.
def calculate():
    global calculation
    result = ""
    if calculation != "":
        try: 
            calculation = str(eval(calculation))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
        except: 
            clear()
            result = "Error"
            text_result.delete(1.0, "end")
            text_result.insert(1.0, result)

# Delete the last character typed from both the text box and the calculation equation. This is executed when the backspace button is pressed.
def backspace():
    global calculation
    x = ""
    text_result.delete("end-2c", "end-1c")
    calculation = calculation[:-1]

# This function prevents the user to type in the text box. The text box was created only for readability.
def disable_text_input(event):
    return "break"

text_result = tk.Text(window, bg='#2A2D36', fg='#FFFFFF', height=1, font=('Arial',32))
text_result.pack()
text_result.bind("<KeyPress>", disable_text_input)

# Create frame for the buttons
buttonframe = tk.Frame(window)

# Set amount of columns
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

# Set amount of rows
buttonframe.rowconfigure(0, weight=1)
buttonframe.rowconfigure(1, weight=1)
buttonframe.rowconfigure(2, weight=1)
buttonframe.rowconfigure(3, weight=1)
buttonframe.rowconfigure(4, weight=1)

# Buttons GUI
clearButton = tk.Button(buttonframe, text="C", font=('Arial',24), bg="orange", fg="white",  command=clear)
clearButton.grid(row=0, column=0, sticky="nsew")

backspaceButton = tk.Button(buttonframe, text="🡨", font=('Arial',24), bg="#0CC0DF", fg="white", activebackground="#0CC0DF", command=backspace)
backspaceButton.grid(row=0, column=1, sticky="nsew")

divideButton = tk.Button(buttonframe, text="/", font=('Arial',24), bg="#0CC0DF", fg="white", activebackground="#0CC0DF", command=lambda: add_symbol("/"))
divideButton.grid(row=0, column=2, sticky="nsew")

multiplyButton = tk.Button(buttonframe, text="x", font=('Arial',24), bg="#0CC0DF", fg="white", activebackground="#0CC0DF", command=lambda: add_symbol("*"))
multiplyButton.grid(row=0, column=3, sticky="nsew")

button7 = tk.Button(buttonframe, text="7", font=('Arial',24), bg="#2A2D36", fg="#FFFFFF", activebackground="#0CC0DF", command=lambda: add_symbol("7"))
button7.grid(row=1, column=0, sticky="nsew")

button8 = tk.Button(buttonframe, text="8", font=('Arial',24), bg="#2A2D36", fg="#FFFFFF", activebackground="#0CC0DF", command=lambda: add_symbol("8"))
button8.grid(row=1, column=1, sticky="nsew")

button9 = tk.Button(buttonframe, text="9", font=('Arial',24), bg="#2A2D36", fg="#FFFFFF", activebackground="#0CC0DF", command=lambda: add_symbol("9"))
button9.grid(row=1, column=2, sticky="nsew")

subtractButton = tk.Button(buttonframe, text="-", font=('Arial',24), bg="#0CC0DF", fg="white", activebackground="#0CC0DF", command=lambda: add_symbol("-"))
subtractButton.grid(row=1, column=3, sticky="nsew")

button4 = tk.Button(buttonframe, text="4", font=('Arial',24), bg="#2A2D36", fg="#FFFFFF", activebackground="#0CC0DF", command=lambda: add_symbol("4"))
button4.grid(row=2, column=0, sticky="nsew")

button5 = tk.Button(buttonframe, text="5", font=('Arial',24), bg="#2A2D36", fg="#FFFFFF", activebackground="#0CC0DF", command=lambda: add_symbol("5"))
button5.grid(row=2, column=1, sticky="nsew")

button6 = tk.Button(buttonframe, text="6", font=('Arial',24), bg="#2A2D36", fg="#FFFFFF", activebackground="#0CC0DF", command=lambda: add_symbol("6"))
button6.grid(row=2, column=2, sticky="nsew")

addButton = tk.Button(buttonframe, text="+", font=('Arial',24), bg="#0CC0DF", fg="white", activebackground="#0CC0DF", command=lambda: add_symbol("+"))
addButton.grid(row=2, column=3, sticky="nsew")

button1 = tk.Button(buttonframe, text="1", font=('Arial',24), bg="#2A2D36", fg="#FFFFFF", activebackground="#0CC0DF", command=lambda: add_symbol("1"))
button1.grid(row=3, column=0, sticky="nsew")

button2 = tk.Button(buttonframe, text="2", font=('Arial',24), bg="#2A2D36", fg="#FFFFFF", activebackground="#0CC0DF", command=lambda: add_symbol("2"))
button2.grid(row=3, column=1, sticky="nsew")

button3 = tk.Button(buttonframe, text="3", font=('Arial',24), bg="#2A2D36", fg="#FFFFFF", activebackground="#0CC0DF", command=lambda: add_symbol("3"))
button3.grid(row=3, column=2, sticky="nsew")

equalsButton = tk.Button(buttonframe, text="=", font=('Arial',24), bg="#0CC0DF", fg="white", activebackground="#0CC0DF", command=calculate)
equalsButton.grid(row=3, column=3, rowspan=2, sticky="nsew")

decimalButton = tk.Button(buttonframe, text=".", font=('Arial',24), bg="#2A2D36", fg="#FFFFFF", activebackground="#0CC0DF", command=lambda: add_symbol("."))
decimalButton.grid(row=4, column=0, sticky="nsew")

button0 = tk.Button(buttonframe, text="0", font=('Arial',24), bg="#2A2D36", fg="#FFFFFF", activebackground="#0CC0DF", command=lambda: add_symbol("0"))
button0.grid(row=4, column=1, columnspan=2, sticky="nsew")

buttonframe.pack(expand=True, fill='both')

window.mainloop()