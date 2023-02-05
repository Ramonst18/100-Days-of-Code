from tkinter import *


def calcular():
    """Funcion que nos convertira las millas a km"""
    millas = int(millas_value.get())
    km = millas * 1.609
    resultado_label.config(text=km)

# Creamos la ventana
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)

# Cremos los labeles
mensaje_label = Label(text="Equivale a", font=("Arial", 16, "bold"))
# mensaje_label.config(text="New Text")
mensaje_label.grid(column=0, row=1)

resultado_label = Label(text="0", font=("Arial", 16, "bold"))
# resultado_label.config(text="New Text")
resultado_label.grid(column=1, row=1)

millas_label = Label(text="Millas", font=("Arial", 16, "bold"))
millas_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 16, "bold"))
km_label.grid(column=2, row=1)

# Creamos los input
millas_value = Entry(width=10)
millas_value.grid(column=1, row=0)

# Creamos los botones
button = Button(text="Calcular", command=calcular)
button.grid(column=1, row=2)

# Mantenemos la ventana
window.mainloop()