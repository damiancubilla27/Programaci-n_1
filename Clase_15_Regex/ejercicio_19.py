'''Cubilla Damian
19. Crear una función llamada validar_password que reciba un string y verifique si
se trata de una contraseña cumple con los requisitos mínimos de seguridad:
- Al menos 8 caracteres
- Al menos una letra mayúscula y una letra minúscula
- Un número
- Un carácter especial
En caso de no cumplir con alguno de los requisitos, imprimir un mensaje
informando cual no se cumplio.
'''
import re 
def validar_password(texto: str):
    if len(texto) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres"

    if not re.search(r'[A-Z]', texto):
        return False, "La contraseña debe contener al menos una letra mayúscula"

    if not re.search(r'[a-z]', texto):
        return False, "La contraseña debe contener al menos una letra minúscula"

    if not re.search(r'[0-9]', texto):
        return False, "La contraseña debe contener al menos un número"

    if not re.search(r'[@!-]', texto):
        return False, "La contraseña debe contener al menos un carácter especial (@, !, -)"

    return True

texto_ingresado = input("Ingrese una contraseña: ")
valido = validar_password(texto_ingresado)

if valido:
    print("Contraseña válida")
else:
    print("Contraseña no válida!!")