from turtle import Turtle


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.left(180)

    def set_color(self, colorName):
        self.color(colorName)

    def position(self, position):
        self.goto(position)

    def move(self, velocity):
        self.forward(velocity)