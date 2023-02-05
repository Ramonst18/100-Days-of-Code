#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
# en readyToSend pondremos letter_for_[name]

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def get_names():
    """Obtendremos la lista de nombres en limpio"""
    # Se obtienen los nombres de los invitados
    file_names = open("Input\\Names\\invited_names.txt", "r")
    list_of_names_without_clean = file_names.readlines()
    clean_list_of_names = list()

    # Se limpia la lista de nombres
    for name in list_of_names_without_clean:
        name = name.strip('\n')
        clean_list_of_names.append(name)

    file_names.close()
    return clean_list_of_names


def get_letters(letter_list_of_names):
    """Se obtendran las cartas a escribir"""
    # Se obtiene la plantilla base de la carta
    file_letter = open("Input\\Letters\\starting_letter.txt", mode="r")
    base_letter = file_letter.read()
    letters = list()

    for name in letter_list_of_names:
        new_letter = base_letter
        modify_letter = new_letter.replace("[name]", name)
        letters.append(modify_letter)

    return letters


def create_letters(letters, list_of_names):
    """Se realiza la creacion de las cartas para los invitados"""
    for index in range(len(list_of_names)):
        name = list_of_names[index]
        letter = letters[index]
        with open(f"Output\\ReadyToSend\\letter_for_{name}", "w") as file:
            file.write(letter)


list_of_names = get_names()
letters = get_letters(list_of_names)
create_letters(letters, list_of_names)

# Se realiza la modificaicon en la plantilla y se crea un archivo nuevo con la plantilla modificada


