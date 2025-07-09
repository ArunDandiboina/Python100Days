import tkinter as tk

window = tk.Tk()
window.title()
window.minsize(200, 200)

# Function to calculate and update the label
def calculate():
    value = float(entry.get() or 0)
    km = value * 1.60934  # Convert miles to kilometers
    label3.config(text=f"{km:.2f}")  # Update the label with the result
    
    
# entry
entry = tk.Entry(width=15)
entry.grid(row=0, column=1)
entry.insert(0, "0")  # Default value

# label
label1 = tk.Label(text="Miles")
label1.grid(row=0, column=2)

# label
label2 = tk.Label(text="is equal to")
label2.grid(row=1, column=0)

# label
label3 = tk.Label(text="0")
label3.grid(row=1, column=1)

# label
label4 = tk.Label(text="Km")
label4.grid(row=1, column=2)

# button
button = tk.Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()