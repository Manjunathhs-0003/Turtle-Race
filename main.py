from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)  # sets up a custamized screen size
user_bet = screen.textinput(
    title="make your bet", prompt="which turtle will win the race? Enter a color: "
)  # pops up a dialouge box on the screen
colors = ["blue", "yellow", "green", "red", "orange", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    t = Turtle()
    t.shape("turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won the race!!!. The winning color was {winning_color}")
            else:
                print(f"you've lost!!!. The {winning_color} is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
