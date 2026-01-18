from turtle import  Turtle,Screen

screen = Screen()
screen.title("Python Etch-a-Sketch")
screen.listen()

def move_forward():
    tim.forward(20)

def turn_left():
    heading = tim.heading()
    tim.setheading(heading-20)

def turn_right():
    heading = tim.heading()
    tim.setheading(heading+20)

screen.onkey(key="Up",fun=move_forward)
screen.onkey(key="Left",fun=turn_left)
screen.onkey(key="Right",fun=turn_right)
screen.onkeypress(key="Up",fun=move_forward)
screen.onkeypress(key="Left",fun=turn_left)
screen.onkeypress(key="Right",fun=turn_right)

tim = Turtle()



screen.exitonclick()
