import tkinter as tk
from datetime import datetime

def calculate_age():
    try:
        birth_date_str = entry.get()
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        current_date = datetime.now()
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Invalid date format. Please use YYYY-MM-DD.")

root = tk.Tk()
root.title("Age Calculator")

input_label = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):")
input_label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
