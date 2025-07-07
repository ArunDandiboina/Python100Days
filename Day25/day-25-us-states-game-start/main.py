import pandas as pd
import turtle

df = pd.read_csv('50_states.csv')

screen = turtle.Screen()
screen.addshape("blank_states_img.gif")

bg_turtle = turtle.Turtle()
bg_turtle.shape("blank_states_img.gif")

guessed_states = []
while len(guessed_states) < 50:
    state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    
    if state is None or state.lower() == "exit":
        missing_states = [state for state in df.state if state not in guessed_states]
        print(missing_states)
        break
    
    x = df[df.state.str.lower() == state.lower()].values
    y = df[df.state.str.lower() == state.lower()].values
    
    if len(x) != 0 and len(y) != 0:
        guessed_states.append(state.title())
        x = x[0, 1]
        y = y[0, 2]
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(int(x), int(y))
        state_turtle.write(state, align="center", font=("Arial", 8, "normal"))

# screen.mainloop()