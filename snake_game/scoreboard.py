# Heredar de la clase tortuga
# Realizar la escritura de texto en la pantalla
# Realizar actualizacion de numero en pantalla
from turtle import Turtle


def load_high_score():
    with open("data.txt", mode="r") as file:
        high_score = file.read()

    return int(high_score)


def write_high_score(score):
    with open("data.txt", mode="w") as file:
        file.write(str(score))


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.penup()
        self.color("white")
        self.score = 0
        self.high_score = load_high_score()
        self.scoreupdate()

    def scoreupdate(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increse_score(self):
        self.score = self.score + 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.scoreupdate()
        write_high_score(self.high_score)

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
