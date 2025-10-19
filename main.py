from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

def move_forward():
    tim.forward(10)

my_screen.listen()
my_screen.onkey(key="space", fun=move_forward)
my_screen.exitonclick()