from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


CoffeeMenu = Menu()
CoffeeMachine = CoffeeMaker()
Dinero_de_maquina = MoneyMachine()
apagar = False

while not apagar:

    drink = input("Que deasea ordenar? " + CoffeeMenu.get_items() + ": ")

    if drink.lower() == "report":
        Dinero_de_maquina.report()
        CoffeeMachine.report()
    elif drink.lower() == "off":
        apagar = True
    else:
        # Obtenemos la informacion de la bebida
        orden = CoffeeMenu.find_drink(drink)

        # Verificamos si hay recursos suficientes
        if CoffeeMachine.is_resource_sufficient(orden):

            # verificamos si alcanza el dinero
            if Dinero_de_maquina.make_payment(orden.cost):

                CoffeeMachine.make_coffee(orden)