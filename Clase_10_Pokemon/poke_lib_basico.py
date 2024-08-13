# MIT License
#
# Copyright (c) 2023 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# importar dentro de los parentesis las funciones necesarias
from poke_lib_elemental import (
    imprimir_mensaje
)

# Escribir debajo las funciones de los enunciados

def buscar_promedio_segun_atributo(lista_pokemones:list[dict], categoria:str, tipo:str)->float:
    if(lista_pokemones != []):
        contador = 0
        suma = 0
        promedio = 0
        for pokemon in lista_pokemones:
            if isinstance(pokemon.get(categoria), list):
                for valor in pokemon[categoria]:
                    if valor == tipo:
                        suma += pokemon.get("poder", 0)
                        contador += 1
                        break
        if contador != 0:
            promedio = suma / contador
            return promedio
        else:
            return -1
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")

def pokedex_promedio_poder_tipo(lista_pokemones:list[dict], categoria:str, tipo:str)->None:
    if(lista_pokemones != []):
        promedio = buscar_promedio_segun_atributo(lista_pokemones, categoria, tipo)
        if(promedio == -1):
            imprimir_mensaje("No se pudo sacar el promedio", "Error")
        else:
            mensaje = f"El poder promedio de pokemones con tipo {tipo} es: {promedio}"
            imprimir_mensaje(mensaje, "Info")
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")