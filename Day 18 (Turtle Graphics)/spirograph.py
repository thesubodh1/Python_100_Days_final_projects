import random
from turtle import  Turtle,Screen

screen = Screen()
screen.title("Spirograph")
colours = ["red","green","blue","black","purple","grey"]
step = 10

timmy = Turtle()
timmy.speed("fastest")
circles = int(360/step)
for i in range(circles):
    timmy.color(random.choice(colours))
    timmy.circle(100)
    timmy.setheading(timmy.heading()+step)








screen.exitonclick()