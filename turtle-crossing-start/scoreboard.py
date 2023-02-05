from turtle import Turtle
FONT = ("Courier", 24, "normal")


# Nos indicará el nivel que estamos actualmente
# además del mensaje de game over cuando perdamos
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Actualizará el nivel del juego actual"""
        self.clear()
        self.level_up()

        # Mandamos el texto a la siguiente posicion
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        """Se actualizará el nivel del juego"""
        self.level += 1

    def game_over(self):
        """Borramos el titulo de level y ponemos el gameover"""
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
