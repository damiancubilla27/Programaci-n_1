''' Cubilla Damian - 1H
16. Crea un diccionario que represente una lista de 
tareas pendientes, donde las claves son las tareas y 
los valores son "True" si están completadas y "False" 
si no lo están. Solicita al usuario el nombre de una 
tarea y modifica el valor para marcarla como completada. 
Imprimir el listado de tareas pendientes
'''
dict_tareas = {"barrer":True, "lavar platos":False, "cocinar":False}
nombre_tarea = input("Ingrese tarea completada: ")
for elemento in dict_tareas.keys():
    if(elemento == nombre_tarea):
        dict_tareas[elemento] = True

for clave, valor in dict_tareas.items():
    if(valor == False):
        print(f"La tarea {clave} tiene como valor {valor}, es decir, esta pendiente")
