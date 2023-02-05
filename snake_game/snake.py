from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

starting_positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    # La tortuga se pondra en la coordenada 0,0 y la siguiente será 20 pixeles a la izquierda
    def __init__(self):
        self.segments = list()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Funcion que creará el cuerpo de la serpiente"""
        for position in starting_positions:
            self.add_segment(position)

    def move(self):
        """Se realizará el movimiento de la serpiente"""
        # start numero en el cual iniciaremos, stop numero en el cual nos detendremos y
        # step seria el incremento o decremento de valores al numero start
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Obtenemos las coordenadas del penultimo segmento
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # movemos el segmento a las corrdenadas del penultimo segmento
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        # Creamos un segmento del cuerpo de la tortuga
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()

        # el segmento es puesto en posicion y almacenado en segmentos
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        # sacamos de pantalla los segmentos de la anterior serpiente.
        for seg in self.segments:
            seg.goto(1000, 1000)

        # Eliminamos el cuerpo de la serpiente y creamos uno nuevo
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())     # Tomamos el ultimo segmento de la lista

    def up(self):
        # Si la cabeza no está apuntando abajo, se realizará el giro
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Si la cabeza no está apuntando arriba, se realizará el giro
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Si la cabeza no está apuntando a la derecha, se realizará el giro
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Si la cabeza no está apuntando a la izquierda, se realizará el giro
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)