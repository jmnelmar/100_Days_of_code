from turtle import Screen, Turtle
MOVE_DISTANCE = 13
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)] 

class Snake:

    def __init__(self):
        self.segments = []
        self.game_is_on = True
        self.make_segments()

    def make_segments(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)    

    def head(self):
        return self.segments[0]

    def add_segment(self, position, color="white"):
        segment = Turtle()
        segment.shape("square")
        # body.shapesize(20,20)
        segment.penup()
        segment.color(color)
        segment.goto(position)
        self.segments.append(segment)

    def extend(self, color="white"):
        #Add new segment to the snake
        self.add_segment(self.segments[-1].position(), color)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)    
        self.segments[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.segments[0].heading() == 0 or self.segments[0].heading() == 180:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() == 180 or self.segments[0].heading() == 0:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(180) 

    def right(self):
        if self.segments[0].heading() == 90 or self.segments[0].heading() == 270:
            self.segments[0].setheading(0) 

    def reset(self):
        self.segments.clear()
        self.make_segments()