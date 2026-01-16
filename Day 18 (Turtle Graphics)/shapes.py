import random
import turtle
from turtle import Turtle,Screen

screen = Screen()
screen.title("Turtle shapes")
timmy = Turtle()
timmy.speed("fastest")

colours = ["red","green","blue","black","purple","grey"]


for i in range(3,10,1):
    timmy.color(random.choice(colours))
    for j in range(i):
        timmy.forward(50)
        timmy.right(360/i)
        timmy.forward(50)





screen.exitonclick()