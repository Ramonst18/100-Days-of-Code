import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Carcamos el interfaz y el jugador
player = Player()
scoreboard = Scoreboard()
carManager = CarManager()

# ejecutamos la parte de escucha y sus teclas
screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.move_cars()

    # Creacion de carros
    if random.randint(0, 6) == 4:
        carManager.create_car()

    # Verificamos si la tortuga llegó al final del camino
    if player.winner():
        player.position()
        scoreboard.update_scoreboard()
        carManager.update_velocity()

    # Verificar colision
    if carManager.verify_player_colission(player):
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
