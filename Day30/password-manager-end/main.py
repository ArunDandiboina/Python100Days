import tkinter as tk
from tkinter import messagebox
import random
import json
import string
import pyperclip

# ---------------------------- SEARCH FUNCTION ------------------------------- #

def search():
    website = website_entry.get()
    
    if not website:
        messagebox.showwarning(title="Warning", message="Please enter a website to search.")
        return
    
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No websites saved yet.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)  # Copy the password to clipboard
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = list(string.ascii_letters)
    symbols = list(string.punctuation)
    numbers = list(string.digits)

    user_password = []

    # print(numbers)
    # print(symbols)
    # print(letters)

    num_letters = random.randint(8, 10)  # Randomly choose number of letters
    num_symbols = random.randint(2, 4)  # Randomly choose number of symbols
    num_numbers = random.randint(2, 4)  # Randomly choose number of numbers

    for _ in range(num_letters):
        user_password.append(random.choice(letters))
    for _ in range(num_symbols):
        user_password.append(random.choice(symbols))
    for _ in range(num_numbers):
        user_password.append(random.choice(numbers))

    random.shuffle(user_password)  # shuffle the password list to randomize order
    final_password = ''.join(user_password)  # join the list into a string
    
    password_entry.delete(0, tk.END)  # Clear the entry field before inserting new password
    password_entry.insert(0, final_password)  # Insert the generated password into the entry field
    pyperclip.copy(final_password)  # Copy the generated password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showwarning(title="Warning", message="Please fill out all fields.")
        return

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    website_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    messagebox.showinfo(title="Success", message="Password saved successfully!")


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas for logo (centered across all columns)
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = tk.Label(text="Website")
website_label.grid(row=1, column=0, padx=5)

email_label = tk.Label(text="Email/Username")
email_label.grid(row=2, column=0, padx=5)

password_label = tk.Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=24)
website_entry.grid(row=1, column=1, padx=5)
website_entry.focus()

email_entry = tk.Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = tk.Entry(width=24)
password_entry.grid(row=3, column=1)

# Buttons
search = tk.Button(text="Search", width=15, command=search)
search.grid(row=1, column=2)

generate_button = tk.Button(text="Generate", width=15, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
