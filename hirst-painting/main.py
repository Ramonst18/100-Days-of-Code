# deberemos de obtener los colores de la imagen, estos deberan de ser
# guardados dentro de una lista y los colores deberan de ser una tupla

import colorgram
import turtle
import random

turtle.colormode(255)

# extraemos 6 colores de la imagen
colors = colorgram.extract("image.jpg", 20)


def get_colors(colors_e):
    """Se obtendrá una lista con los colores en rgb"""
    colors_list = list()
    for color in colors_e:
        rgb = color.rgb

        tupla = get_tupla(rgb)
        colors_list.append(tupla)
    return colors_list


def get_tupla(rgb):
    """Se obtendrá y regresará la tupla del color
    Se debe de agregar el color rgb"""
    r = rgb.r
    g = rgb.g
    b = rgb.b
    tupla = (r, g, b)

    return tupla


colors_list = get_colors(colors)
print(colors_list)

### Parte 2 del proyecto
# Se deberá de pintar manchitas en un cuadrado 10 manchitas de alto y 10 manchitas de ancho
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
# movemos a la tortuga para indicar en donde empezará a pintar
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")


def nueva_linea():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


for dot_count in range(1, number_of_dots + 1):
    # pintamos un punto con eleccion aleatorea de color
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    # si la cantidad de puntos es divicible entre 10, se creará una nueva linea
    if dot_count % 10 == 0:
        nueva_linea()



screen = turtle.Screen()
screen.exitonclick()
