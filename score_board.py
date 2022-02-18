from turtle import Turtle
FONT=('courier',14,'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-210,210)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Level:{self.level}", align='left', font=FONT)

    def increase_level(self):
        self.level+=1
        self.update_score()

    def game_over(self):
        self.goto(-50,0)
        self.write(f"Game over", align='left', font=FONT)
