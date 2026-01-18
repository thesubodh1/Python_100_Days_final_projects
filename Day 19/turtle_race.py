import time
from turtle import Turtle,Screen
import  random

screen = Screen()
screen.setup(width=600,height=600)
screen.title("Turtle Race")
colours = ["red","blue","black","green","yellow"]
coordinates = [(-280,-180),(-280,-80),(-280,20),(-280,120),(-280,220)]
my_turtles = []
race_is_on = False
screen.tracer(0)
user_bet = screen.textinput(title="Choose a winning turtle",prompt="which turtle is going to win the race").lower()

for item in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(coordinates[item])
    new_turtle.color(colours[item])
    my_turtles.append(new_turtle)

if user_bet:
    race_is_on = True
while race_is_on:
    screen.update()
    time.sleep(0.1)
    for turtle in my_turtles:
        if turtle.xcor() < 280:
            turtle.forward(random.randint(0,10))
        else:
            race_is_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("Congrats!! your turtle won the race")
            else:
                print(f"Oops!! {winner} won the race")
screen.exitonclick()