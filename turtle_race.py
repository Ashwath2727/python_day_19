import random
from turtle import Turtle, Screen

my_screen = Screen()
colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple"
]
y_positions = [-60, -20, 20, 60, 90, 120]
is_race_on = False
all_turtles = []

my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color : ")
print(user_bet)

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])

    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False

            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You have WON! The  {winning_color} turtle is the winner!")
            else:
                print(f"You have LOST! The  {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


my_screen.exitonclick()