from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        starting_position = 0
        for position in range(3):
            new_segment = Turtle("square")
            new_segment.color("pink")
            new_segment.penup()
            new_segment.goto(starting_position, 0)
            starting_position -= 20
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("pink")
        new_segment.penup()
        new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

