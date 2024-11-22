import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        miles = float(miles_entry.get())
        gallons = float(gallons_entry.get())
        if gallons != 0:
            mpg = miles / gallons
            result_label.config(text=f"MPG: {mpg:.2f}")
        else:
            messagebox.showerror("Error", "Gallons cannot be zero.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("MPG Calculator")

miles_label = tk.Label(root, text="Miles on a Full Tank:")
miles_label.grid(row=0, column=0, padx=10, pady=10)

miles_entry = tk.Entry(root)
miles_entry.grid(row=0, column=1, padx=10, pady=10)

gallons_label = tk.Label(root, text="Gallons of Gas:")
gallons_label.grid(row=1, column=0, padx=10, pady=10)

gallons_entry = tk.Entry(root)
gallons_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate MPG", command=calculate_mpg)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="MPG: ")
result_label.grid(row=3, column=0, columnspan=2)


root.mainloop()

