# Dibujar un triangulo, cuadrado, pentagono, hexagono
# heptagono, octagono, nonagono y decagono
# cada lado tendrá 100 en longitud
# una vuelta completa son 360 grados
# con cada lado de la figura se tendra que dividir entre los 360 para
# obtener cuanto será el angulo para cada lado de la figura actual
import random
from turtle import Turtle, Screen

tommy_turtle = Turtle()


def draw_figure(sides):
    # Iniciamos el lado actual en 0 y obtenemos el angulo de la figura actual
    actual_side = 0
    anguloFigura = 360 / sides

    # mientras el lado actual no supere al numero de lados
    while actual_side < sides:
        tommy_turtle.forward(100)
        tommy_turtle.right(anguloFigura)
        actual_side += 1


screen = Screen()

# Recorreremos todos los lados totales de las figuras descritas con anterioridad
for lados in range(3, 11):
    tommy_turtle.color(random.choice(["Red", "Green"]))
    draw_figure(lados)


screen.exitonclick()



