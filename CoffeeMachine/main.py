# podemos usar el to-do en mayusculas y sin guion para mencionar las tareas faltantes
from Data import resources, MENU

machine_On = True


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]

    print(f"Water: {water}ml \n"
          f"Milk: {milk}ml \n"
          f"Coffee: {coffee}g \n"
          f"Money: ${money} \n")


def prepare_coffee(drink):
    dictionary_drink = MENU[drink.lower()]
    ingredients = dictionary_drink["ingredients"]
    there_are_resources = verify_resources(ingredients)

    # Si hay recursos disponibles se ejecutaran las ordenes
    if there_are_resources:
        # Seccion de introducir dineros
        cent1 = int(input("how many pennies? (0.01): "))
        cent5 = int(input("how many nickels? (0.05): "))
        cent10 = int(input("how many dimes? (0.10): "))
        cent25 = int(input("how many quarter? (0.25): "))
        total_cost = dictionary_drink["cost"]

        reach, change = verify_money(cent1, cent5, cent10, cent25, total_cost)

        if reach:
            update_resources(ingredients, total_cost)

            # si hay cambio
            if change > 0:
                print(f"Order complete, here is ${round(change, 2)} dollars in change.")
            else:
                print("Order complete.")


def verify_resources(drink_resources):
    """"Verifica los recursos disponibles en la maquina y devuelve
    si hay recursos o no"""
    water = drink_resources["water"]
    coffee = drink_resources["coffee"]
    milk = 0

    # Verificamos si ocupa leche la bebida
    if "milk" in drink_resources:
        milk = drink_resources["milk"]

    # Lower than
    if water > resources["water"]:
        print("Insufficient water")
        return False

    if coffee > resources["coffee"]:
        print("Insufficient coffee")
        return False

    if milk > resources["milk"]:
        print("Insufficient milk")
        return False

    return True


def update_resources(ingredients, total_cost):
    total_water = resources["water"]
    total_milk = resources["milk"]
    total_coffee = resources["coffee"]
    total_money = resources["money"]

    # it does the operations
    total_water = total_water - ingredients["water"]

    if "milk" in ingredients:
        total_milk = total_milk - ingredients["milk"]

    total_coffee = total_coffee - ingredients["coffee"]
    total_money = total_money + total_cost

    # save the information
    resources["water"] = total_water
    resources["milk"] = total_milk
    resources["coffee"] = total_coffee
    resources["money"] = total_money


def verify_money(cent1, cent5, cent10, cent25, total_cost):
    """Verificará si hay sificiente dinero para realizar la compra
    regresará si alcanza y cuanto le sobra"""
    total_money = (cent1 * 0.01) + (cent5 * 0.05) + (cent10 * 0.1) + (cent25 * 0.25)
    change = total_money - total_cost

    # Si le falta dinero
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False, 0
    else:
        return True, change


while machine_On:
    drink_answer = input("What would you like? (espresso/latte/cappuccino): ")
    if drink_answer.lower() == "off":
        machine_On = False
    elif drink_answer.lower() == "report":
        report()
    else:
        prepare_coffee(drink_answer)
