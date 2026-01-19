import time
from turtle import  Screen
from  snake import  Snake
from food import Food
from scoreboard import  ScoreBoard

screen = Screen()
screen.setup(height=600,width=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(key="Up",fun=snake.move_up)
screen.onkey(key="Left",fun=snake.move_left)
screen.onkey(key="Right",fun=snake.move_right)
screen.onkey(key="Down",fun=snake.move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.reset()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with walls
    if snake.head.xcor() <  -280 or snake.head.xcor () > 280 or snake.head.ycor() <  -280 or snake.head.ycor () > 280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()