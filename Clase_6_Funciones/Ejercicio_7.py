''' Cubilla Damian - 1H
Crear una función que calcule el máximo común divisor de dos números. 
Recibe dos parámetros (números) y devuelve el máximo común divisor.
'''
def calcular_maximo_comun(numero_uno:int, numero_dos:int)->int:
    while numero_dos != 0:
        numero_uno, numero_dos = numero_dos, numero_uno % numero_dos
    return numero_uno
numero_uno_ingresado = int(input("Ingrese numero: "))
numero_dos_ingresado = int(input("Ingrese otro numero: "))
print(f"El maximo comun divisor es: {calcular_maximo_comun(numero_uno_ingresado, numero_dos_ingresado)}")