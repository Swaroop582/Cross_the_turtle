from turtle import Turtle
import random

COLORS=["red","yellow","pink","green","purple"]
START_MOVE_DISTANCE=5
INCREMENT_MOVE=5

class carManager:
    def __init__(self):
        self.allcars=[]
        self.carspeed=START_MOVE_DISTANCE

    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==6:
           new_car = Turtle("square")
           new_car.shapesize(stretch_len=2,stretch_wid=1)
           new_car.penup()
           new_car.color(random.choice(COLORS))
           random_y =random.randint(-180,180)
           new_car.goto(240,random_y)
           self.allcars.append(new_car)

    def move_cars(self):
        for cars in self.allcars:
            cars.backward(self.carspeed)

    def level_up(self):
        self.carspeed+=INCREMENT_MOVE



