# import csv

# abrimos el archivo y metemos todas las lineas en data
# with open("weather_data.csv", "r") as file:
#    data = file.readlines()


# with open("weather_data.csv", "r") as file:
#    # Con importar la libreria csv, podemos lograr leer nuestro archivo csv
#    # De una manera limpia
#    data = csv.reader(file)
#    temperatures = []

#    # Recorremos los datos para agregar la temperatura a la lista de temperaturas
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))

        # temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

# Obtenemos la informacion contenida en el archivo
# data = pandas.read_csv("weather_data.csv")


# Imprimirmos la c olumna temp
# print(data["temp"])

# Convertimos la informacion a un diccionario
# data_dict = data.to_dict()

# Cambiamos una columna de datos a lista
# temp_list = data["temp"].to_list()

# Obtenemos la temperatura promedio
# temperatureTotal = 0

# Obtenemos la temperatura en total
# for temperature in temp_list:
#    temperatureTotal += temperature

# Obtenemos el promedio
# avgTemperature = temperatureTotal / len(temp_list)

# print(int(avgTemperature))

# Forma corta de obtener la temperatura promedio
# average = sum(temp_list) / len(temp_list)
# print(average)

# Forma de hacerlo desde data

# print(data["temp"].mean())

# Obtenemos el numero maximo
# print(data["temp"].max())

# get data in Columns
# print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])

# print("--------------------------------------")

# Imprimimos la fila completa con la temperatura mas alta
# print(data[data.temp == data.temp.max()])

# Obtenemos los datos del lunes
# monday = data[data.day == "Monday"]

# obtenemos la informacion de la condicion del lunes
# print(monday.condition)

# Cambiamos los celsius a fahrenheit
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)


# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# Creamos un nuevo DataFrame
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")

# se creará un archivo llamado squierrel_count_csv en el cual tendremos una tabla con lo siguente
# una columna con los colores que solo pueden ser grey, Cinnamon y black, además de otra columna
# en donde estaran su cantidad
# los colores serán tomados de la columna Primary Fur Color

# Obtenemos los datos del archivo csv
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


# Obtenemos la columna de los colores
column_color = data["Primary Fur Color"]

# Obtenemos las cantidades por color, y ordenadas de mayor a menor cantidad
counts = column_color.value_counts(dropna=False)

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [counts[0], counts[1], counts[2]]
}

# Creamos el dataframe y creamos el archivo
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
