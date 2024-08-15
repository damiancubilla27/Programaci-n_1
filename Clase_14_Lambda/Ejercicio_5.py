''' Cubilla Damian - 1H
5. Encuentra el diccionario con el valor más alto de una clave específica.
'''
alumnos = [
    {'nombre': 'Ana', 'nota': 8},
    {'nombre': 'Juan', 'nota': 5},
    {'nombre': 'Luis', 'nota': 9}
]
mejor_alumno = max(alumnos, key=lambda x: x['nota'])
print(mejor_alumno) 