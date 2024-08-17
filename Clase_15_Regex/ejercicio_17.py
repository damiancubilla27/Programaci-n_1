'''Cubiilla Damian
17. Crear la función validar_patente que reciba un string como parámetro y
devuelva True en caso de tratarse de un número de patente válido o False en
caso contrario. Debe poder admitir estos dos tipos:
'''
import re
def validar_patente(texto:str)->bool:
    resultado = re.match("^([A-Z]{2} [0-9]{3} [A-Z]{2})$|^([A-Z]{3} [0-9]{3})$", texto)
    return resultado

texto_ingresado = input("Ingrese patente: ")
if validar_patente(texto_ingresado):
    print("La patente es correcta!")
else:
    print("La patente es INCORRECTA.")