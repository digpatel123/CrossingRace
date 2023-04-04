import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_player, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.new_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_player_crossed():
        player.start_player()
        car_manager.speed_up()
        scoreboard.level_up()

screen.exitonclick()
