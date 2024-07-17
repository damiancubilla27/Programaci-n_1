''' Cubilla Damian - 1H
9. Crea un diccionario que contenga las capitales de los 
países de América del Sur. Luego, pide al usuario que 
ingrese el nombre de un país y muestra su capital 
correspondiente.
'''
dict_capitales = {"Argentina":"Buenos aires", "Chile":"Santiago", "Peru":"Lima"}
pais_ingresada = input("Ingrese un pais para buscar su capital: ")
for elemento in dict_capitales.keys():
    if(elemento == pais_ingresada):
        print(f"{dict_capitales[elemento]}")