''' Cubilla Damian - 1H
Escribir una función que tome un nombre y un apellido y devuelva un email en
formato "inicial_nombre.apellido@utn-fra.com.ar".
Por ejemplo Facundo Falcone: f.falcone@utn-fra.com.ar
'''
def crear_diccionario_nombres(texto:str)->str:
    lista = texto.split(" ")
    letra_inicial = lista[0][0]
    retorno = f"{letra_inicial}.{lista[1]}@utn-fra.com.ar"
    return retorno

texto_ingresado = input("Ingrese nombre y apellido: ")
print(crear_diccionario_nombres(texto_ingresado))