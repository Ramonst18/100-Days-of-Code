from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


# activamos el escucha de la pantalla
screen.listen()

# si la tecla dentro del parentesis es presionada se ejecutará la funcion de adentro
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()