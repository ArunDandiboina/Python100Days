# best practle - import screen and turtle separately
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)
    
def turn_left():
    t.left(10)
    
def turn_right():
    t.right(10)
    
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
    
screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(clear, "c")
screen.listen()
# end
screen.mainloop()


# Higher Order Functions
# A function that takes another function as an argument
# and executes inside the function
