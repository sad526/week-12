import tkinter as tk

# Functionality
def increase():
    global count
    count += 1          
    label.config(text=str(count))

def decrease():
    global count
    count -= 1
    label.config(text=str(count))

def reset():
    global count
    count = 1
    label.config(text=str(count))

# Main window
window = tk.Tk()
window.title("Counter App")
window.geometry("300x200")

count = 22

# Buttons and label
frame = tk.Frame(window)
frame.pack(pady=20)
 
btn_increase = tk.Button(frame, text="+", font=("Arial", 16), width=5, command=increase)
btn_increase.grid(row=0, column=0, padx=10)

label = tk.Label(frame, text=str(count), font=("Arial", 16), width=5)
label.grid(row=0, column=1)

btn_decrease = tk.Button(frame, text="-", font=("Arial", 16), width=5, command=decrease)
btn_decrease.grid(row=0, column=2, padx=10)

btn_reset = tk.Button(window, text="Reset", font=("Arial", 12), command=reset)
btn_reset.pack(pady=10)

window.mainloop()
