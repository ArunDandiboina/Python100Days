# interface
# widgets - elements of the GUI

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Widgets Examples")
window.minsize(500, 300)

# label widget
label = tk.Label(text="This is a label", font=("Arial", 24, "bold"))
label.pack()

# button widget
button = tk.Button(text="Click Me", command=lambda: label.config(text=entry.get()), font=("Arial", 12))
button.pack()

# entry widget
entry = tk.Entry(width=30)
entry.pack()

# text widget
# text = tk.Text(height=2, width=30)
# text.pack()

# other widgets
# spinbox, scale, checkbutton, radiobutton, listbox, messagebox

# spinbox widget
spinbox = tk.Spinbox(from_=0, to=10, width=5, command=lambda: label.config(text=spinbox.get()))
spinbox.pack()

# scale widget
scale = tk.Scale(from_=0, to=100, orient='horizontal', command=lambda x: label.config(text=f"Scale Value: {x}"))
scale.pack()
# print(scale.get())  # Get the current value of the scale

# checkbutton widget
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(text="Check me", variable=check_var, command=lambda:
    label.config(text=f"Checkbutton is {'checked' if check_var.get() else 'unchecked'}"))
checkbutton.pack()

# radiobutton widget
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option 1", variable=radio_state,
                                value=1, command=lambda: label.config(text=f"Selected: {radio_state.get()}"))
radiobutton1.pack()

# listbox widget - 2 items
def on_listbox_select(event):
    selected_item = listbox.get(listbox.curselection())
    label.config(text=f"Selected: {selected_item}")

listbox = tk.Listbox(height=4)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.bind('<<ListboxSelect>>', on_listbox_select)
listbox.pack()


# messagebox widget
def show_message():
    messagebox.showinfo("Info", "This is a message box")

message_button = tk.Button(text="Show Message", command=show_message)
message_button.pack()


    
window.mainloop()