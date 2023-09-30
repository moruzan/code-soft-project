import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task, get_task_color())
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Warning", "Select a task to remove!")

def get_task_color():
    return "black"  # You can customize the color here

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

add_button = tk.Button(root, text="Add Task", command=add_task, bg='lightblue', font=("Arial", 12))
add_button.grid(row=0, column=2, padx=10, pady=10)

listbox = tk.Listbox(root, selectbackground='lightblue', font=("Arial", 14), selectmode=tk.SINGLE, width=40, height=10)
listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg='lightcoral', font=("Arial", 12))
remove_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
