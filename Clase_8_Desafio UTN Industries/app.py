# MIT License
#
# Copyright (c) 2024 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
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

# llamar aca cada una de las funciones con prefijo 'utn_' para usarlas en el cuerpo del match
from utn_biblioteca import (
    limpiar_consola,
    utn_imprimir_nombres_personajes, utn_imprimir_nombres_alturas,
    utn_calcular_imprimir_heroe, utn_calcular_imprimir_promedio_dato, 
    utn_menu_principal, utn_imprimir_personajes_debajo_promedio,
    utn_imprimir_cantidad_personajes, utn_imprimir_empresa,
    utn_imprimir_dato_por_genero, utn_imprimir_identidad,
    utn_imprimir_valor_por_orden
)

def utn_personajes_app(lista_personajes: list[dict]) -> None:
    while True:
        match utn_menu_principal():
            case 1:
                utn_imprimir_nombres_personajes(lista_personajes)
            case 2:
                utn_imprimir_nombres_alturas(lista_personajes)
            case 3:
                utn_calcular_imprimir_heroe(lista_personajes, "maximo", "altura")
            case 4:
                utn_calcular_imprimir_heroe(lista_personajes, "minimo", "altura")
            case 5:
                utn_calcular_imprimir_promedio_dato(lista_personajes, "altura")  
            case 6:
                utn_imprimir_identidad(lista_personajes, "maximo", "altura")
                utn_imprimir_identidad(lista_personajes, "minimo", "altura")
            case 7:
                utn_calcular_imprimir_heroe(lista_personajes, "maximo", "peso")
                utn_calcular_imprimir_heroe(lista_personajes, "minimo", "peso")
            case 8:
                utn_calcular_imprimir_heroe(lista_personajes, "maximo", "poder")
                utn_calcular_imprimir_heroe(lista_personajes, "minimo", "poder")
            case 9:
                utn_calcular_imprimir_promedio_dato(lista_personajes, "poder")
                utn_imprimir_personajes_debajo_promedio(lista_personajes, "poder") 
            case 10:
                utn_imprimir_cantidad_personajes(lista_personajes)
            case 11:
                utn_imprimir_empresa(lista_personajes, "DC Comics")
                utn_imprimir_empresa(lista_personajes, "Marvel Comics")
            case 12:
                utn_imprimir_valor_por_orden(lista_personajes, "poder", False)
            case 13:
                utn_imprimir_valor_por_orden(lista_personajes, "inteligencia", True)
            case 14:
                utn_imprimir_dato_por_genero(lista_personajes, "poder", "F")
            case 15:
                utn_imprimir_dato_por_genero(lista_personajes, "poder", "M")
            case 16:
                break
            case _:
                print('Opción inválida')
        limpiar_consola()