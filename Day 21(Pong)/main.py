import time
from turtle import Screen
from paddle import  Paddles
from ball import  Ball
from  scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.title("Python Pong")
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

paddles = Paddles()
ball = Ball()
score = ScoreBoard()

screen.onkey(key="w",fun=paddles.move_left_up)
screen.onkey(key="s",fun=paddles.move_left_down)
screen.onkey(key="Up",fun=paddles.move_right_up)
screen.onkey(key="Down",fun=paddles.move_right_down)

game_is_on = True

while game_is_on:
    screen.update()
    ball.bounce_ball()

    # detect collision with  paddles
    if paddles.right_paddle.distance(ball) < 30 or paddles.left_paddle.distance(ball) < 30:
        ball.bounce_x()

    # detect collision on top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect if paddle is missed
    if ball.xcor() > 280:
        score.l_point()
        ball.reset_ball()

    if ball.xcor() < -280:
        score.r_point()
        ball.reset_ball()

screen.exitonclick()