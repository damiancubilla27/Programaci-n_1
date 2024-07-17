''' Cubilla Damian - 1H
11. Crea un diccionario que represente una lista de tareas por hacer. 
Cada clave del diccionario debe ser el nombre de una tarea y cada 
valor debe ser su estado (los estados son:  pendiente, en proceso, 
completada). Imprimir todas las tareas seguido de su estado.
'''
dict_tareas = {"barrer":"pendiente", "lavar platos":"en proceso", "cocinar":"completada"}
for clave, valor in dict_tareas.items():
    print(f"{clave}  ---  {valor}")