from turtle import Turtle
from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# Es el generador de automoviles
class CarManager:

    def __init__(self):
        self.listCars = list()
        self.velocityNumber = STARTING_MOVE_DISTANCE

    def create_car(self):
        newCar = Car()
        newCar.set_color(random.choice(COLORS))
        posicionY = random.randint(-230, 230)
        newCar.goto(300, posicionY)
        self.listCars.append(newCar)

    def move_cars(self):
        for car in self.listCars:
            car.move(self.velocityNumber)
            if car.xcor() == -320:
                self.listCars.remove(car)

    def verify_player_colission(self, player):
        for car in self.listCars:
            if player.distance(car) < 25:
                return True

    def update_velocity(self):
        self.velocityNumber += MOVE_INCREMENT