import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    try:
        minutes = int(minutes_entry.get())
        if minutes < 0:
            messagebox.showerror("Error", "Minutes cannot be negative.")
            return
        rate = rate_var.get()
        if rate == "Daytime":
            charge = minutes * 0.02
        elif rate == "Evening":
            charge = minutes * 0.12
        elif rate == "Off-Peak":
            charge = minutes * 0.05
        messagebox.showinfo("Charge", f"The charge for the call is: ${charge:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of minutes.")


root = tk.Tk()
root.title("Long-Distance Calls")


rate_var = tk.StringVar(value="Daytime")

daytime_radio = tk.Radiobutton(root, text="Daytime (6:00 A.M. to 5:59 P.M.)", variable=rate_var, value="Daytime")
daytime_radio.grid(row=0, column=0, padx=10, pady=5)

evening_radio = tk.Radiobutton(root, text="Evening (6:00 P.M. to 11:59 P.M.)", variable=rate_var, value="Evening")
evening_radio.grid(row=1, column=0, padx=10, pady=5)

offpeak_radio = tk.Radiobutton(root, text="Off-Peak (midnight to 5:59 A.M.)", variable=rate_var, value="Off-Peak")
offpeak_radio.grid(row=2, column=0, padx=10, pady=5)

minutes_label = tk.Label(root, text="Enter Minutes:")
minutes_label.grid(row=3, column=0, padx=10, pady=10)

minutes_entry = tk.Entry(root)
minutes_entry.grid(row=3, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Charge", command=calculate_charge)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()
