'''Cubilla Damian
8. Crear una función que reciba una lista de palabras y devuelva otra lista con
las palabras que comienzan con la letra ‘U’
'''
import re
def devolver_palabras_con_U(lista:list)->list:
    nueva_lista = []
    for elemento in lista:
        nuevo_elemento = re.sub(r"^[a-zA-Z]", "U", elemento)
        nueva_lista.append(nuevo_elemento)
    return nueva_lista

lista_de_palabras = ["Hola","chau","Todo","bien"]
print(devolver_palabras_con_U(lista_de_palabras))