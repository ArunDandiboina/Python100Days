import tkinter as tk
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

time = None

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
except pd.errors.EmptyDataError:
    df = pd.DataFrame("data/french_words.csv")

word_sets = df.to_dict(orient="records")
word_set = ''

def is_known():
    word_sets.remove(word_set)
    df = pd.DataFrame(word_sets)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    
def flip_card():
    global word_set
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(text, text=word_set['English'], fill="white")

def next_card():
    global word_set
    global time
    if time:
        window.after_cancel(time)
    word_set = random.choice(word_sets)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(text, text=word_set['French'], fill="black")
    time = window.after(3000, flip_card)
    
    
# ------------------ UI Setup ------------------ #

window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# cavas for card
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
text = canvas.create_text(400, 263, text="French", font=("Ariel", 40, "italic"), fill="black")
next_card()  # Show the first card immediately
canvas.grid(row=0, column=0, columnspan=2, pady=10)

# buttons for right and wrong
right_img = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)  

wrong_img = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

window.mainloop()