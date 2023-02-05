### Lectura de archivo
# Abrimos un archivo y almacenamos su contenido en una variable
with open("my_file.txt") as file:
    # Realizamos la lectura del archivo y este regresa un string
    contents = file.read()
    print(contents)

    # Cerramos el archivo, esto para recuperar los recursos utilizados
    # a la hora de abrir el archivo
    # file.close()


### Escritura de archivo
# Debemos de poner el modo escritura poniendo el mode="w", este sustituira el texto
# Para no perder el texto, debemos de poner el mode="a" para añadir contenido
# with open("my_file.txt", mode="w") as file:
    # escritura de archivo
#    file.write("\nNew text.")
