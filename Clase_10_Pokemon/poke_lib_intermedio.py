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
    imprimir_mensaje, nombre_format_pokemon
)

# Escribir debajo las funciones de los enunciados
def tiene_varios_atributo(dict_poke:dict, key:str)->bool:
    retorno = None
    if isinstance(dict_poke.get(key), list):
        if(len(dict_poke[key]) > 1):
            retorno = True
        else:
            retorno = False
    return retorno

def podekex_pokemones_varios_atributo(lista_pokemones:list[dict], key:str)->None:
    if(lista_pokemones != []):
        for elemento in lista_pokemones:
            if(tiene_varios_atributo(elemento, key)):
                imprimir_mensaje(nombre_format_pokemon(elemento), "Info")
            else:
                continue
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")

def pokemones_atributo_y_cantidad(lista_pokemones:list[dict], key:str)->list[dict]:
    if(lista_pokemones != []):
        lista_pokemones_mas_atributos = []
        for elemento in lista_pokemones:
            if(tiene_varios_atributo(elemento, key)):
                lista_pokemones_mas_atributos.append(elemento)
            else:
                continue
        return lista_pokemones_mas_atributos
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")

def imprimir_nombre_cantidad_atributo(lista_pokemones:list[dict], key:str)->None:
    if(lista_pokemones != []):
        for elemento in lista_pokemones:
            texto = f"{nombre_format_pokemon(elemento)} - Cantidad de {key}: {len(elemento[key])}"
            imprimir_mensaje(texto, "Info")
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")

def pokedex_pokemones_atributo_y_cantidad(lista_pokemones:list[dict], key:str)->None:
    if(lista_pokemones != []):
        lista_varios_atributos = pokemones_atributo_y_cantidad(lista_pokemones, key)
        imprimir_nombre_cantidad_atributo(lista_varios_atributos, key)
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")