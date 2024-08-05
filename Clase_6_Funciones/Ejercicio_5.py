''' Cubilla Damian - 1H
Crear una función que determine si un número es primo o no. 
Recibe un parámetro (número) y devuelve True si es primo 
y False si no lo es.
'''
def calcular_primo(numero:int)->bool:
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero_ingresado = int(input("Ingrese numero: "))
if(calcular_primo(numero_ingresado)):
    print(f"El numero {numero_ingresado} es primo")
else:
    print(f"El numero {numero_ingresado} no es primo")
