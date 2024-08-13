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
    imprimir_mensaje,nombre_format_pokemon, capitalizar_palabras
)

# Escribir debajo las funciones de los enunciados
def obtener_atributos_pokemon(dict_poke:dict, key:str)->int:
    if(key in dict_poke):
        return len(dict_poke[key])
    else:
        return len(dict_poke[key])

def pokedex_imprimir_multiples_atributos(lista_pokemones:list[dict], key:str)->None:
    if(lista_pokemones != []):
        for elemento in lista_pokemones:
            texto = f"{nombre_format_pokemon(elemento)} - {key}: "
            if(obtener_atributos_pokemon(elemento, key) > 0):
                datos = " | ".join(elemento[key])
                texto_final = texto + datos
                texto_final = capitalizar_palabras(texto_final)
                imprimir_mensaje(texto_final, "Info")
            else:
                vacia = "No posee"
                segundo_texto_final = texto + vacia
                segundo_texto_final = capitalizar_palabras(segundo_texto_final)
                imprimir_mensaje(segundo_texto_final, "Info")
                
    else:
        imprimir_mensaje("Lista de pokemones vacia", "Error")