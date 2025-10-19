from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_clockwise():
    tim.right(10)

def turn_anticlockwise():
    tim.left(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

my_screen.listen()
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="a", fun=turn_anticlockwise)
my_screen.onkey(key="d", fun=turn_clockwise)
my_screen.onkey(key="c", fun=clear_screen)

my_screen.exitonclick()