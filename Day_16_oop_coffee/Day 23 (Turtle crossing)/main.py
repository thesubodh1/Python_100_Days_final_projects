import time
from turtle import Screen
from race_cars import  RaceCars
from race_turtle import RaceTurtle
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Python Turtle crossing")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

car = RaceCars()
race_turtle = RaceTurtle()
scoreboard = ScoreBoard()

screen.onkey(key="Up",fun=race_turtle.move_up)
screen.onkey(key="Down",fun=race_turtle.move_back)


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    # detect level-up
    if race_turtle.ycor() > 280:
        car.level_up()
        race_turtle.level_up()
        scoreboard.update_score()

    # detect collision with cars
    for car_ in car.cars:
        if race_turtle.distance(car_) < 30:
            game_is_on = False
            scoreboard.game_over()








screen.exitonclick()