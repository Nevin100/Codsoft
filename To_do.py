# TO DO TASK

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(task_index, {'bg':'light green'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack()

button_add = tk.Button(frame_buttons, text="Add Task", width=12, command=add_task)
button_add.grid(row=0, column=0)

button_delete = tk.Button(frame_buttons, text="Delete Task", width=12, command=delete_task)
button_delete.grid(row=0, column=1)

button_mark = tk.Button(frame_buttons, text="Mark as Completed", width=15, command=mark_task)
button_mark.grid(row=0, column=2)

listbox_tasks = tk.Listbox(root, height=15, width=50, border=0)
listbox_tasks.pack()

root.mainloop()
