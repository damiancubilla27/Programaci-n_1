''' Cubilla Damian - 1H
9. Escribir un programa que le pida al usuario que ingrese una letra, y 
luego imprima "Es una vocal" si la letra es una vocal (a, e, i, o, u), 
o "Es una consonante" si la letra es una consonante'''
letra_ingresada = input("Ingrese una letra: ")
if letra_ingresada == 'a' or letra_ingresada == 'e' or letra_ingresada == 'i' or letra_ingresada == 'o' or letra_ingresada == 'u':
    print("Es una vocal")
else:
    print("Es una consonante")