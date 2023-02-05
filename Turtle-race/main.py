from turtle import Turtle, Screen
import random

is_race_on = False

# Pantalla
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Cuál tortuga ganará la carrera? digita un color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

turtles = list()
# cargamos las tortugas
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-225, y=y_positions[turtle_index])
    turtles.append(new_turtle)

if user_bet.lower() in colors:
    is_race_on = True

while is_race_on:

    # Recorreremos la lista de tortugas
    for turtle in turtles:
        # Tomaremos la distancia en entre un numero de 0 a 10
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        # Si la tortuga llega a la meta y además la carrera aun está en curso
        if turtle.xcor() > 230 and is_race_on:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()
