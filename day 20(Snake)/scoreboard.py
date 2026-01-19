from turtle import  Turtle

ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-20,260)
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over\nFinal Score: {self.score}",align=ALIGNMENT,font=FONT)

