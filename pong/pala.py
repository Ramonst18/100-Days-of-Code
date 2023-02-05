from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        # Creamos la pala del jugador
        self.shape("square")
        self.color("white")
        self.penup()

        # Dimenciones de la pla
        self.shapesize(5, 1)

    def position(self, tupla):
        """Se mandará la pala a una posicion en pantalla"""
        # Posicion de la pala
        self.goto(tupla)

    def go_up(self):
        """Moverá hacia arriba la pala"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moverá hacia abajo la pala"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
