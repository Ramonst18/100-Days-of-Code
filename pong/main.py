from turtle import Screen
from pala import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Creamos la pantalla
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# apagamos la actualizacion de pantalla
screen.tracer(0)

# Creamos las palas, pelotas y las mandamos a su posicion
r_paddle = Paddle()
l_paddle = Paddle()
ball = Ball()
r_paddle.position((350, 0))
l_paddle.position((-350, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detectamos la colision con la parte superior de la ventana y la parte inferior
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()

    # Detect collison with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect ball collison with the screen border of R paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect ball collision with the screen border of L paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
