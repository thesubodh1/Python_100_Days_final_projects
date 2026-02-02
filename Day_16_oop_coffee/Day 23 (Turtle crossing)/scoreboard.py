from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super(). __init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score:{self.score}",align="center",font=("Arial",24,"bold"))

    def update_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over\nFinal Score:{self.score}",align="center",font=("Arial",24,"bold"))