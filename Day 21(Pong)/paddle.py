from turtle import Turtle

class Paddles:
    def __init__(self):
        self.left_paddle = self.create_paddle((-280,0))
        self.right_paddle = self.create_paddle((280,0))


    def create_paddle(self,location):
        paddle = Turtle(shape="square")
        paddle.penup()
        paddle.color("white")
        paddle.shapesize(stretch_len=1,stretch_wid=5)
        paddle.goto(location)
        return  paddle

    def move_left_up(self):
        if self.left_paddle.ycor() < 280:
            self.left_paddle.goto(self.left_paddle.xcor(),self.left_paddle.ycor() + 20)

    def move_left_down(self):
        if self.left_paddle.ycor() > -280:
            self.left_paddle.goto(self.left_paddle.xcor(), self.left_paddle.ycor() - 20)

    def move_right_up(self):
        if self.right_paddle.ycor() < 280:
            self.right_paddle.goto(self.right_paddle.xcor(), self.right_paddle.ycor() + 20)

    def move_right_down(self):
        if self.right_paddle.ycor() > -280:
            self.right_paddle.goto(self.right_paddle.xcor(), self.right_paddle.ycor() - 20)

