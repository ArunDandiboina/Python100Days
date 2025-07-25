import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quiz_brain):
        self.quiz_brain = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 14, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Quiz Completed!", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280, justify="center")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30, padx=30)
        self.get_next_question()

        true_image = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0, pady=15)

        false_image = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, pady=15)

        self.window.mainloop()
    
    def get_next_question(self):
        q_text = self.quiz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
    
    def enable_buttons(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
    
    def show_correct(self):
        self.canvas.config(bg="green")
        self.window.after(1000, self.reset_canvas)
    
    def show_incorrect(self):
        self.canvas.config(bg="red")
        self.window.after(1000, self.reset_canvas)
    
    def reset_canvas(self):
        self.enable_buttons()
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.question_text, text=f"🎉 Quiz Completed!\nThanks for playing!\n\nFinal Score: {self.quiz_brain.score}/{self.quiz_brain.question_number}")
            self.disable_buttons()
    
    def true_pressed(self):
        self.disable_buttons()
        is_right = self.quiz_brain.check_answer("True")
        if is_right:
            self.show_correct()
        else:
            self.show_incorrect()
        self.update_score()
        
    def false_pressed(self):
        self.disable_buttons()
        is_right = self.quiz_brain.check_answer("False")
        if is_right:
            self.show_correct()
        else:
            self.show_incorrect()
        self.update_score()
        
    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")