import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
count_down = None  # Initialize countdown variable
# work
# break
# work
# break
# work
# break
# work
# long break.

# ---------------------------- POP UP ------------------------------- #
def show_popup(message):
    popup = tk.Toplevel()
    popup.title("Pomodoro Alert")
    popup.config(padx=20, pady=20, bg=YELLOW)
    popup.attributes("-topmost", True)
    
    label = tk.Label(popup, text=message, font=(FONT_NAME, 20, "bold"), fg=RED, bg=YELLOW)
    label.pack()

    btn = tk.Button(popup, text="OK", command=popup.destroy, bg=GREEN, fg=YELLOW)
    btn.pack(pady=10)
    
    # automatically close the popup after 5 seconds
    popup.after(5000, popup.destroy)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global count_down
    reps = 0
    canva.itemconfig(timer, text="00:00")
    label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    
    # reset button disable
    reset_button.config(state="disabled")
    start_button.config(state="normal")
    window.after_cancel(count_down)  # Cancel the countdown if it's running

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    start_button.config(state="disabled")
    reset_button.config(state="normal")

    if reps % 8 == 0:
        show_popup("Long Break Time!")
        countdown(LONG_BREAK_MIN * 60)
        label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        show_popup("Break Time!")
        countdown(SHORT_BREAK_MIN * 60)
        label.config(text="Break", fg=PINK)
    else:
        if reps != 1:
            show_popup("Work Time!")
        countdown(WORK_MIN * 60)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global count_down
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canva.itemconfig(timer, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        count_down = window.after(1000, countdown, count - 1)
    else:
        start_timer()  # Automatically start the next timer
        # Update checkmark label
        checkmark_label.config(text="✔" * (reps // 2))  # Update checkmarks based on completed work sessions
            
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canva = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canva.create_image(100, 112, image=tomato_img)
timer = canva.create_text(100, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))

canva.grid(column=1, row=1, pady=10)

# label
label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label.grid(column=1, row=0)

# buttons
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2, pady=15)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2, pady=15)

# styling buttons
start_button.config(bg=GREEN, fg=YELLOW, font=(FONT_NAME, 10, "bold"))
reset_button.config(bg=RED, fg=YELLOW, font=(FONT_NAME, 10, "bold"))

reset_button.config(state="disabled")  # Initially disable the reset button

# checkmark label
checkmark_label = tk.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark_label.grid(column=1, row=3)

window.mainloop()