import tkinter as tk
import random
import string

def generate():
    length = int(length_entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def reset():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Generator")
root.geometry('410x200')

# Add background color
root.configure(bg='lightgray')

length_label = tk.Label(root, text="Password Length:", bg='lightgray', font=('Arial', 12))
length_label.pack(pady=5)
length_entry = tk.Entry(root, width=50, font=('Arial', 12))
length_entry.pack(pady=5)

password_label = tk.Label(root, text="Generated Password:", bg='lightgray', font=('Arial', 12))
password_label.pack(pady=5)
password_entry = tk.Entry(root, width=50, font=('Arial', 12))
password_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate, bg='lightblue', font=('Arial', 12))
generate_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset, bg='lightcoral', font=('Arial', 12))
reset_button.pack(pady=5)

root.mainloop()
