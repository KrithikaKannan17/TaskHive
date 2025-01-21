import tkinter as tk
from tkinter import messagebox
import pickle

# Initialize main window
root = tk.Tk()
root.title("TaskHive – Buzz through your tasks effortlessly!")
root.geometry("450x550")
root.configure(bg="#ffefd5")  

# Task list display with scrollbar
frame = tk.Frame(root, bg="#ffefd5")
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
task_listbox = tk.Listbox(frame, width=50, height=15, bg="#ffffff", fg="#0000ff", selectbackground="#ff4500", activestyle="none", yscrollcommand=scrollbar.set) 
scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Task input field
task_entry = tk.Entry(root, width=45, font=("Arial", 12))
task_entry.pack(pady=5)

# Functions to handle tasks
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.pkl", "wb") as f:
        pickle.dump(tasks, f)
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.pkl", "rb") as f:
            tasks = pickle.load(f)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

# Buttons
btn_frame = tk.Frame(root, bg="#ffefd5")
btn_frame.pack(pady=10)

btn_add = tk.Button(btn_frame, text="Add Task", command=add_task, bg="#ff0000", fg="white", width=12)  
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_remove = tk.Button(btn_frame, text="Remove Task", command=remove_task, bg="#0000ff", fg="white", width=12) 
btn_remove.grid(row=0, column=1, padx=5, pady=5)

btn_complete = tk.Button(btn_frame, text="Mark Completed", command=mark_completed, bg="#ff4500", fg="black", width=12)  
btn_complete.grid(row=1, column=0, padx=5, pady=5)

btn_clear = tk.Button(btn_frame, text="Clear All", command=clear_tasks, bg="#ffa500", fg="white", width=12)  
btn_clear.grid(row=1, column=1, padx=5, pady=5)

btn_save = tk.Button(root, text="Save Tasks", command=save_tasks, bg="#ff0000", fg="white", width=40) 
btn_save.pack(pady=5)

btn_load = tk.Button(root, text="Load Tasks", command=load_tasks, bg="#0000ff", fg="white", width=40)  
btn_load.pack(pady=5)

# Keyboard bindings
root.bind("<Return>", lambda event: add_task())
root.bind("<Delete>", lambda event: remove_task())
root.bind("<Control-s>", lambda event: save_tasks())
root.bind("<Control-l>", lambda event: load_tasks())

# Load existing tasks
load_tasks()

# Start the GUI loop
root.mainloop()
