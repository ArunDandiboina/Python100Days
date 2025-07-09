# Geometry Manager.

import tkinter as tk

# Function to handle button click
def button_clicked():
    label.config(text=entry.get())
    entry.delete(0, tk.END)
    
window = tk.Tk()
window.title("Geometry Manager")
window.minsize(200, 200)

# label
label = tk.Label(text="This is a label", font=("Arial", 24))
label.config(text="New Text")
# label.pack()
# label.place(x=50, y=50) 
label.grid(row=0, column=1)

# button
button = tk.Button(text="Click Me", command=button_clicked)
# button.pack()
# button.place(x=0, y=0) 
button.grid(row=1, column=1, padx=100)

# entry
entry = tk.Entry(width=20)
# entry.pack()
# entry.place(x=50, y=100) 
entry.grid(row=2, column=1)


window.mainloop()