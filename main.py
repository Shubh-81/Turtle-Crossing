import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    screen.update()
    if player.ycor() > 280:
        car.level_up()
        player.reset_pos()
        score.level+=1
        score.update_board()

    for c in car.cars:
        if(player.distance(c) < 20):
            score.show_game_over()
            game_is_on = False
    
    time.sleep(0.1)
    car.create_car()
    car.move_cars()



screen.exitonclick()
