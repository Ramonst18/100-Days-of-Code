# como crear una clase, el cada palabra de la clase debe de empezar con mayusculas
class User:
    # La palabra pass nos sirve para saltar a la siguiente linea de codigo
    # El constructor __init__ es la clase especial para iniciar la informacion y/o variables iniciales
    def __init__(self, user_id, username):
        # Esta clase es siempre llamada cuando se crea un objeto
        # Con el self, creamos las variables que solo se podran utilizar dentro de la clase, al menos que
        # se pidan, es normal que los nombres de los parametros sean igual a los de los atributos
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        # si vamos a crear atributos en nuestra clase, no es necesario recibir datos sobre el en parametros
        # si sabemos como estará por default, lo podemos crear y de eso podemos añadirle un valor

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "Pedro")

print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
