import tkinter as tk
from tkinter import messagebox

service_prices = {
    "Oil Change": 30.00,
    "Lube Job": 20.00,
    "Radiator Flush": 40.00,
    "Transmission Fluid": 100.00,
    "Inspection": 35.00,
    "Muffler Replacement": 200.00,
    "Tire Rotation": 20.00
}

def calculate_total():
    total = 0
    for service, price in service_prices.items():
        if service_vars[service].get() == 1:
            total += price
    total_label.config(text=f"Total: ${total:.2f}")


root = tk.Tk()
root.title("Joe's Automotive Service")


service_vars = {}
for idx, service in enumerate(service_prices):
    service_vars[service] = tk.IntVar()
    tk.Checkbutton(root, text=service, variable=service_vars[service]).grid(row=idx, column=0, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total)
calculate_button.grid(row=len(service_prices), column=0, pady=10)

total_label = tk.Label(root, text="Total: $0.00")
total_label.grid(row=len(service_prices)+1, column=0, pady=10)


root.mainloop()


