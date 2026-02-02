from turtle import Turtle

class RaceTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("blue")
        self.setheading(90)
        self.shapesize(stretch_wid=2,stretch_len=2)
        self.goto(0,-280)

    def move_up(self):
        self.forward(20)

    def move_back(self):
        if self.ycor() > -280:
            self.backward(20)

    def level_up(self):
        self.goto(0,-280)


