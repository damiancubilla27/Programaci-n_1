''' Cubilla Damian - 1H
20. Crea un diccionario que represente los asientos de un avión, 
donde las claves son los números de asientos y los valores son 
"True" si están ocupados y "False" si no lo están. Solicita al 
usuario un número de asiento y modifica su valor para marcarlo 
como ocupado. Luego imprimí la lista de asientos libres
'''
dict_asientos = {1:True, 3:False, 4:False, 5:True, 6:True}
numero_asiento_ingresado =int(input("Ingrese numero de asiento: "))
for elemento in dict_asientos.keys():
    if(elemento == numero_asiento_ingresado):
        dict_asientos[elemento] = False

for clave, valor in dict_asientos.items():
    if(valor == True):
        print(f"El asiento {clave} se encuentra libre")