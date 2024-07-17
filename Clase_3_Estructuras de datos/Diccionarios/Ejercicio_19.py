''' Cubilla Damian - 1H
19. Crea un diccionario que represente las temperaturas de 
una ciudad durante una semana, donde las claves son los 
días de la semana y los valores son las temperaturas 
correspondientes. Calcula la temperatura promedio de 
la semana.
'''
dict_dias = {"lunes":30, "martes":25, "miercoles":31, "jueves":22, "viernes":25, "sabado":26, "domingo":17}
suma = 0
promedio = 0
for elemento in dict_dias.keys():
    suma += dict_dias[elemento]
promedio = suma / len(dict_dias)
print(f"El promedio de la temperatura en la semana es: {promedio}")
