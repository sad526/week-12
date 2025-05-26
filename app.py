import tkinter as tk
from tkinter import ttk

def save_task():
    event = event_entry.get()
    priority = priority_var.get()
    output_box.delete("1.0", tk.END)  # Clear previous text
    output_box.insert(tk.END, f"Event: {event}\nPriority: {priority}\n")

# Main Window
root = tk.Tk()
root.title("To-Do App")
root.geometry("350x300")

# Event label and entry
tk.Label(root, text="Event", font=("Times new roman", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
event_entry = tk.Entry(root, width=25)
event_entry.grid(row=0, column=1, padx=10)

# Priority label and dropdown
tk.Label(root, text="Priority", font=("Times new roman", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
priority_var = tk.StringVar()
priority_dropdown = ttk.Combobox(root, textvariable=priority_var, values=["Low", "Medium", "High"], state="readonly", width=22)
priority_dropdown.grid(row=1, column=1, padx=10)
priority_dropdown.current(0)  # Set default to "Low"

# Save Button
save_btn = tk.Button(root, text="Save", command=save_task, bg="Green", fg="white", width=15)
save_btn.grid(row=2, column=0, columnspan=2, pady=15)

# Editable Text Box
output_box = tk.Text(root, height=5, width=40)
output_box.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
