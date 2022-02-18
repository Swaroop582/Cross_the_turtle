from turtle import Turtle
START=(0,-200)
MOVE=10
FINISH_Y=230

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE)

    def go_to_start(self):
        self.goto(START)

    def is_at_finish(self):
        if self.ycor()>FINISH_Y:
            return True
        else:
            return False










