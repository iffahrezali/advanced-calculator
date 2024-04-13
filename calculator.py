import tkinter as tk

def update_display(value):
    button = equation.get()
    if button == '0':
        equation.set(value)
    else:
        equation.set(button + value)

def clear_display():
    equation.set("0")

def calculate_display():
    try:
        result = eval(equation.get())
        equation.set(result)
    except Exception as e:
        equation.set("Error")

calculator = tk.Tk()
calculator.title("Calculator")
equation = tk.StringVar()
entry = tk.Entry(calculator, textvariable=equation, font=("Helvetica",20))
entry.grid(row=0, column=0, columnspan=6, pady=6)

button_list = [
     ("0", 1, 0), ("1", 1, 1), ("2", 1, 2), ("3", 1, 3), 
     ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("7", 2, 3), 
     ("8", 3, 0), ("9", 3, 1), (".", 3, 2), ("+", 3, 3),
     ("-", 4, 0), ("x", 4, 1), ("/", 4, 2), ("=", 4, 3),
     ("log", 5, 0), ("ln", 5, 1), ("10^x", 5, 2), ("e^x", 5, 3), 
     ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), 
     ("sin^-1", 7, 0), ("cos^-1", 7, 1), ("tan^-1", 7, 2)
 ]       

for (text, row, col) in button_list:
    button = tk.Button(calculator, text=text, width=5, font=("Helvetica",20), command=lambda t=text: update_display(t) if t != '=' else calculate_display())
    button.grid(row=row, column=col)

clear_button = tk.Button(calculator, text="Clear", width=5, font=("Helvetica", 20), command=clear_display)
clear_button.grid(row=6, column=3, columnspan=3)

calculator.mainloop()

