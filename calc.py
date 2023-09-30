import tkinter as tk

def evaluate_expression():
    try:
        result = str(eval(entry.get()))
        result_label.config(text="Result: " + result, fg="green")
    except Exception as e:
        result_label.config(text="Error", fg="red")

# Create the main window
root = tk.Tk()
root.title("Colorful Python Calculator")
root.geometry("400x400")

# Entry widget for input
entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 16))
result_label.grid(row=1, column=0, columnspan=4)

# Button colors
button_bg = "#4CAF50"  # Green
button_fg = "white"
button_font = ("Arial", 16)

# Buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 2, 0

for button_text in buttons:
    tk.Button(root, text=button_text, width=5, height=2, font=button_font,
              bg=button_bg, fg=button_fg, command=lambda b=button_text: entry.insert(tk.END, b) if b != '=' else evaluate_expression()).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the GUI
root.mainloop()
    