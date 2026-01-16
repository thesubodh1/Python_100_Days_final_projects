import turtle
from turtle import  Screen
import random


turtle.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b)
    return colour

screen = Screen()
screen.title("Spot painting")

tim = turtle.Turtle()

def take_position():
    tim.penup()
    tim.setheading(270)
    tim.forward(250)
    tim.setheading(180)
    tim.forward(250)
    tim.setheading(0)

def move_up():
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

take_position()
for i in range(10):
    for j in range(10):
        tim.color(random_colour())
        tim.dot(20)
        tim.forward(50)
    move_up()

tim.hideturtle()








screen.exitonclick()