from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in POSITION:
            self.add_segment(i)

    def add_segment(self, position):
        seg = Turtle('circle')
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)


