import turtle
from turtle import Turtle, Screen
import random

tommy_turtle = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple_color = (r, g, b)
    return tuple_color


directions = [0, 90, 180, 270]
tommy_turtle.pensize(10)
tommy_turtle.speed("fastest")

screen = Screen()
for _ in range(0, 500):
    color = random_color()
    tommy_turtle.pencolor(color)
    tommy_turtle.forward(30)
    tommy_turtle.setheading(random.choice(directions))

screen.exitonclick()
