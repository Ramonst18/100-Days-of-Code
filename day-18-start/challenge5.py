# dibujar varios circulos desde el centro de la panbtalla
import turtle
from turtle import Turtle, Screen
import random

tom = Turtle()
# Ponemos que el color será tomado hasta los 255 colores
turtle.colormode(255)
screen = Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple_color = (r, g, b)
    return tuple_color


angulo = 10
tom.speed("fastest")

while angulo < 360:
    color = random_color()
    tom.pencolor(color)
    tom.circle(50)
    tom.right(10)
    angulo += 10

screen.exitonclick()
