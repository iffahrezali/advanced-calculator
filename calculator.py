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
     ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("4", 1, 3), ("5", 1, 4),
     ("6", 2, 0), ("7", 2, 1), ("8", 2, 2), ("9", 2, 3), ("0", 2, 4),
     ("sin", 3, 0), ("cos", 3, 1), ("tan", 3, 2), (".", 3, 3), ("+", 3, 4),
     ("-", 4, 0), ("x", 4,1), ("/", 4, 2), ("=", 4, 3)
 ]       

for (text, row, col) in button_list:
    button = tk.Button(calculator, text=text, padx=40, pady=40, font=("Helvetica",20), command=lambda t=text: update_display(t) if t != '=' else calculate_display())
    button.grid(row=row, column=col)

clear_button = tk.Button(calculator, text="Clear", padx=20,pady=20, font=("Helvetica", 20), command=clear_display)
clear_button.grid(row=4, column=4, columnspan=3)

calculator.mainloop()

