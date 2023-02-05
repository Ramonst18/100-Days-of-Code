from turtle import Turtle, Screen

tommy_turtle = Turtle()

screen = Screen()

for _ in range(6):
    tommy_turtle.forward(10)
    tommy_turtle.penup()
    tommy_turtle.forward(10)
    tommy_turtle.pendown()

screen.exitonclick()
