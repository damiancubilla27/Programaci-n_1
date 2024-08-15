import json
from ejemplo_tres import Personaje

lista_dicionario = []
lista_personajes = list[Personaje]()

path = 'C:\\Users\\User\\Desktop\\Cursada Actual\\Clase_13_POO\\ProyectosFinalizados.json'
with open(path, 'r', encoding='utf-8') as file:
    lista_dicionario = json.load(file)

for diccionario in lista_dicionario:
    # Normalizar las claves del diccionario
    diccionario_normalizado = {
        "id": diccionario.get("id"),
        "nombre": diccionario.get("Nombre del Proyecto", diccionario.get("nombre")),
        "descripcion": diccionario.get("Descripción", diccionario.get("descripcion")),
        "fecha_inicio": diccionario.get("Fecha de inicio", diccionario.get("fecha_inicio")),
        "fecha_final": diccionario.get("Fecha de Fin", diccionario.get("fecha_final")),
        "presupuesto": diccionario.get("Presupuesto", diccionario.get("presupuesto")),
        "estado": diccionario.get("Estado", diccionario.get("estado"))
    }
    personaje = Personaje(**diccionario_normalizado)
    lista_personajes.append(personaje)

for personaje in lista_personajes:
    personaje.saludar()