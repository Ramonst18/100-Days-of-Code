student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas

# Lectura del archivo y creacion del dataframe
student_data_frame = pandas.DataFrame(pandas.read_csv("nato_phonetic_alphabet.csv"))

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #print(row)
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

# Forma 1
# dictionary = {}
for (index, row) in student_data_frame.iterrows():
    #dictionary[row.letter] = row.code
    pass

# Forma 2
# Creaccion del diccionario apartir del dataframe
dictionary = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}
print(dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter a word: ")

# obtenemos cada letra de la palabra escrita por el usuario y obtenemos el valor de esa letra en el diccionario
word_in_code = [dictionary[word.upper()] for word in user_word]
print(word_in_code)
