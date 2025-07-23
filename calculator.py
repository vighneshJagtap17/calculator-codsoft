import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Input field
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to append value to entry
def press(num):
    entry.insert(tk.END, num)

# Function to evaluate the expression
def equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), bg="#4CAF50", fg="white",
                  command=equal).grid(row=row, column=col, padx=5, pady=5)
    elif text == 'C':
        tk.Button(root, text=text, width=22, height=2, font=('Arial', 18), bg="#f44336", fg="white",
                  command=clear).grid(row=row, column=col, columnspan=4, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                  command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
