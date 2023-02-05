from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    # cancelamos el timmer y reiniciamos los valores
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timmer.config(text="Timer", fg=GREEN)
    label_check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Verificamos las repeticiones y asignamos los tiempos
    if reps % 2 == 1 or reps == 1:
        label_timmer.config(text="Work", fg=GREEN)
        # Repeticion para 1, 3, 5, 7 ... Work
        count_down(work_sec)
    elif reps % 8 == 0:
        label_timmer.config(text="Break", fg=RED)
        # Large Break
        count_down(long_break_sec)
    else:
        label_timmer.config(text="Break", fg=PINK)
        # repeticion para 2, 4, 6, 8, ... small break
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    # Obtenemos los minutos a partir de los segundos
    count_min = math.floor(count / 60)

    # Obtenemos los segundos
    count_sec = count % 60

    # Parte para mostrar bien los segundos, o sea con doble digito
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Tenemos que llamar a canvas y llamar al metodo de configuracion de item,
    # Esto para poder modificar la configuracion del elemento que esté en nuestro canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # Despues de un segundo, se realizará la resta del contador
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        # cada dos repeticiones se pondrá una palomita
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        label_check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# Ventana
window = Tk()
window.title("Pomodoro")
# fg para cambiar el color de letras
# agregamos un padding y cambiamos el fondo
window.config(padx=100, pady=50, bg=YELLOW)


# Toma la cantidad de tiempo que se debe de esperar, realiza la ejecucion de una funcion y se pasa los argumentos
# window.after(1000, say_something, "Patata", 7)

# canvas, para poder poner un lienzo en nuestra ventana, tenemos que dar las dimenciones de este
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# para crear una clase de PhotoImage y poder usar la imagen despues
tomato_img = PhotoImage(file="tomato.png")

# añadimos la imagen al canvas, se pueden poner multiples cosas en el canvas
# Tenemos que dar la posicion en donde estará y que es lo que pondremos
canvas.create_image(100, 112, image=tomato_img)

# Creamos un texto que será nuestro contador
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# mandamos nuestro canvas a la ventana
canvas.grid(row=1, column=1)

# Creamos los Label
label_timmer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
label_timmer.grid(row=0, column=1)

label_check = Label(bg=YELLOW, fg=GREEN)
label_check.grid(row=4, column=1)

# Creamos los botones
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)


window.mainloop()