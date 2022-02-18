import time
from turtle import Screen
from player import Player
from car_manager import carManager
from score_board import Scoreboard

screen=Screen()
screen.setup(width=500,height=500)
screen.title("Turtle - cross game")
screen.tracer(0)

player=Player()
car=carManager()
score=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")
game_is_on=True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    #detect collision with the cars

    for i in car.allcars:
        if i.distance(player) < 20:
            game_is_on=False
            score.game_over()

    #detect successful reaching
    if player.is_at_finish():
        player.go_to_start()
        car.level_up()
        score.increase_level()






screen.exitonclick()