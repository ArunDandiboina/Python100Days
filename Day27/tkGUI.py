# History of GUI - 
# First GUI was created by Alan Kay in 1970s Xero PARC
# Xerox - Ethernet, GUI, WYSIWYG, Object Oriented Programming, mouse, Bitmapped Display
# Next - macintosh in 1984
# Next - Windows 3.1 in 1992

import tkinter as tk

window = tk.Tk()
window.title("My First GUI")
window.minsize(500, 300)

# Create a label
label = tk.Label(text="Heading", font=("Arial",24 , "bold"))
label.pack()
# side = 'top', 'bottom', 'left', 'right'
# gemoetry manager - pack, grid, place

# config method to change properties of the label
label.config(text="New Text", font=("Arial", 12, "normal"))


# end
window.mainloop()