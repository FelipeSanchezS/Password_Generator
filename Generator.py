import string
import random

longitud = int(input("Ingrese la longitud de la contraseña: "))

#Agregamos todso los simbolos, letras y numeros de odnde se creara la contraseña 
caracteres = string.ascii_letters + string.digits + string.punctuation

#Elije caracteres aleatorios que esten dentro de la variable caracteres
contraseña = "".join(random.choice(caracteres)
for i in range(longitud))

print("La contraseña generada por el sistema es: "+contraseña)