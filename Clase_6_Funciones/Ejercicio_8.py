''' Cubilla Damian - 1H
Crear una función que verifique si un número es par o impar. 
Recibe un número como parámetro y devuelve True si es par o False si es impar.
'''
def calcular_par_impar(numero:int)->bool:
    if(numero % 2 == 0):
        return True
    else:
        return False
numero_ingresado = int(input("Ingrese numero: "))
if(calcular_par_impar(numero_ingresado)):
    print(f"El numero {numero_ingresado} es PAR")
else:
    print(f"El numero {numero_ingresado} es IMPAR")