from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)


colors = ["red", "orange", "yellow", "green", "blue", "purple",
          "pink", "brown", "black", "white", "cyan", "magenta",
          "gold", "silver", "navy", "lime"]
user_bet = screen.textinput(
    title="Make your bet",
    prompt=f"Choose a color:\n{colors}\nEnter your bet:"
)

num = screen.textinput(
    title="Turtle number",
    prompt="Enter the number of turtles from 2 to 16: "
)

num = int(num)

while num < 2 or num > 16:
    num = screen.textinput(
        title="Turtle number",
        prompt="The number of turtles should be from 2 to 16: "
    )
    num = int(num)

y_position = -220
all_turtles = []

for turtle_index in range(num):
    tim = Turtle()
    tim.shape("turtle")

    banna = colors[turtle_index]
    tim.color(banna)

    tim.penup()
    tim.goto(x=-230, y=y_position)

    all_turtles.append(tim)

    y_position += 30

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            is_race_on = False

            winning_color = turtle.pencolor()

            print(f"{winning_color} turtle won the race!")

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()
