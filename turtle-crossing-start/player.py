from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Será la tortuga que nosotros moveremos
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.position()
        self.left(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def position(self):
        """Mandamos a la posicion inicial"""
        self.goto(STARTING_POSITION)

    def winner(self):
        """Verificamos si llegó la tortuga a la poscion de meta"""
        if self.ycor() == FINISH_LINE_Y:
            return True
