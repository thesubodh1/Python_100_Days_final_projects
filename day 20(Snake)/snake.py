from turtle import Turtle

INITIAL_COORDINATES = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for cords in INITIAL_COORDINATES:
            self.add_segments(cords)


    def add_segments(self,coordinates):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(coordinates)
        self.segments.append(new_segment)

    def extend(self):
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        new_position = (new_x,new_y)
        self.add_segments(new_position)


    def move(self):
        for segment in range(len(self.segments)-1,0,-1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)






