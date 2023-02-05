from turtle import Turtle

# Pelota
# Dimensiones
# width = 20, height = 20
# Posicion de inicio
# x_pos = 0, y_pos = 0
# Cuando la pantalla se actualice la pelota se moverá
# automaticamente en la pantalla y se movera hacia arriba y derecha
# con cada actualizacion, la posicion cambiará


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.movingX = 10
        self.movingY = 10
        self.move_speed = 0.1

    def move(self):
        """Realizamos el movimiento de la pelota"""
        currentx = self.xcor()
        currenty = self.ycor()
        self.goto(currentx + self.movingX, currenty + self.movingY)

    def bounce_y(self):
        """Aplicamos el rebote en la posicion superior e inferior de la pantalla"""
        # Cambiamos la direccion de movimiento
        self.movingY *= -1

    def bounce_x(self):
        """Aplicamos el rebote hacia izquierda o derecha cuando suceda la
        colision con algun paddle"""
        # Cambiamos la direccion de movimiento
        self.movingX *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reinicia la posicion de la pelota moviendola al centro y mueve la pelota
        a direccion contraria con la cual colisionó con el borde"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
