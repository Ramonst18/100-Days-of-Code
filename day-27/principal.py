from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# relleno a las partes exteriores, puede servir para centrar los elementos
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Tambien se puede aplicar la separacion entre componentes usando el pad
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

# el pack se encarga de empaquetar cada uno de los widgets, siempre comenzara en la parte superior centro
# Se puede modificar dando la posicion dentro del .pack()

# Place es de posicionamiento preciso, se da los valores de X y Y dentro del place()
# es dificil de usar cuando se poseen mas elementos

# El grid trabaja como si fuera una cuadricula que podemos dividir en cualquier numero de
# columnas y renglones, se dara la posicion de la columna y de la fila dentro de .grid()
# Es relativo, es facil de trabajar, no se pueden mezclar .pack con .grid




window.mainloop()