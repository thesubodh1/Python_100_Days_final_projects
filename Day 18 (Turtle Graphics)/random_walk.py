import random
from turtle import Screen
import turtle

screen = Screen()
screen.title("Random Walk")

turtle.colormode(255)
tim = turtle.Turtle()
tim.width(10)
tim.speed(20)
angles = [0,90,180,270]

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b)
    return colour

for _ in range(1000):
    tim.forward(20)
    tim.color(random_colour())
    tim.setheading(random.choice(angles))

screen.exitonclick()



