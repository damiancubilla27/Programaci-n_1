''' Cubilla Damian - 1H
Escribir una función que tome un número de tarjeta de crédito como input,
verificar que todos los caracteres sean numéricos y devolver los últimos
cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** ****
**** 1234"
'''
def verificar_numeros(texto: str)->str:
    if texto.isdigit():
        return '*' * (len(texto) - 4) + texto[-4:]
    else:
        return "Número de tarjeta inválido. Asegúrese de que todos los caracteres sean numéricos."

numero_tarjeta = "1234567812345678"
resultado = verificar_numeros(numero_tarjeta)
print(resultado) 