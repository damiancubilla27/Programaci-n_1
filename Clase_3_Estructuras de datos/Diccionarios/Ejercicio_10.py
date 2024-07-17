''' Cubilla Damian - 1H
10. Crea un diccionario que represente las notas de un examen 
de varios estudiantes, donde las claves son los nombres de los 
estudiantes y los valores son sus notas. Imprime el promedio 
de las notas.
'''
dict_notas = {"Alan":3, "Tiziano":6, "Maia":9}
suma = 0
promedio = 0
for elemento in dict_notas.keys():
    suma += dict_notas[elemento]
promedio = suma / len(dict_notas)
print(f"El promedio del curso es: {promedio}")
