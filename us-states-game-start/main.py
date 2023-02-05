import turtle
import pandas

# Cargamos la ventana y la imagen que tendrá nuestra ventana
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Cargamos el archivo con la información
data = pandas.read_csv("50_states.csv")
statesList = data.state.to_list()
correctStates = list()
score = 0

game_is_on = True
while game_is_on:
    # Verificamos si el score es distinto de 0 para realizar un cambio en la parte superior de la ventana
    if score != 0:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    else:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    # Se cerrará el juego cuando escribamos exit
    if answer_state.capitalize() == "Exit":
        # Creamos la lista de los estados faltantes
        misingStates = [state for state in statesList if (state not in correctStates)]

        # Creamos un nuevo DataFrame que nos servirá para llenar un archivo csv y creamos ese archivo
        new_data = pandas.DataFrame(misingStates)
        new_data.to_csv("states_to_learn.csv")
        break

    # Verificamos si el estado recibido está en la lista de estados
    if answer_state.capitalize() in statesList:
        # Verificamos si ya no se ha escrito el estado anteriormente
        if answer_state.capitalize() not in correctStates:
            # verificamos la respuesta recibida y obtenemos las coordenadas
            state_data = data[data.state == answer_state.capitalize()]
            x = float(state_data.x)
            y = float(state_data.y)

            # Creamos la turtuga de tipo texto y la mandamos a la posicion correspondiente en el mapa
            stateTurtle = turtle.Turtle()
            stateTurtle.hideturtle()
            stateTurtle.penup()
            stateTurtle.goto(x, y)
            stateTurtle.write(answer_state)

            # Aumentamos la puntuacion
            score += 1

            # Verificamos que la puntuacion haya llegado a su meta
            if score == 50:
                game_is_on = False

            # Agregamos el estado correcto a la lista de estados ya recibidos
            correctStates.append(answer_state.capitalize())

            screen.update()

# states_to_learn.csv

