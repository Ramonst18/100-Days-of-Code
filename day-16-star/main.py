# import another_module
# from turtle import Turtle, Screen
# # print(another_module.another_variable)
#
# timmy = Turtle()
#
# timmy.shape("turtle")
# timmy.color("cyan")
# my_screen = Screen()
#
# timmy.forward(100)
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

# creamos una tabla
table = PrettyTable()

# añadimos datos a la tabla
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# formato a la tabla
table.align = "l"

print(table)
