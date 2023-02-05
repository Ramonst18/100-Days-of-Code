from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Teclas a usar
# La W será para moverse hacia adelante
# la S será para moverse hacia atras
# La A será para girar a la izquierda
# La D será para girar a la derecha
# La tecla C será para borrar el dibujo realizado


def move_forwards():
    tim.forward(10)


def turn_right():
    tim.right(15)


def turn_left():
    tim.left(15)


def move_backward():
    tim.back(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# activamos el escucha de la pantalla
screen.listen()

# si la tecla dentro del parentesis es presionada se ejecutará la funcion de adentro
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()




