'''Cubilla Damian
12. Crear una función llamada obtener_oraciones que reciba como parámetro un
string y que devuelva una lista con las oraciones (delimitadores, ‘.’, ‘!’, ‘?’).
Ejemplo de texto: https://onlinegdb.com/UMdr3hI3G
'''
import re
def obtener_oraciones(texto:str)->list:
    oraciones = re.split(r'[.¿!?]', texto)
    return oraciones

texto = "¿Bello es mejor que feo? Explícito es mejor que implícito. Simple es mejor que complejo. Complejo es mejor que complicado. Plano es mejor que anidado. Espaciado es mejor que denso. La legibilidad es importante. Los casos especiales no son lo suficientemente especiales como para romper las reglas. Sin embargo la practicidad le gana a la pureza. Los errores nunca deberían pasar silenciosamente. A menos que se silencien explícitamente. Frente a la ambigüedad, evitar la tentación de adivinar. Debería haber una, y preferiblemente solo una, manera obvia de hacerlo. A pesar de que eso no sea obvio al principio a menos que seas Holandés. Ahora es mejor que nunca. A pesar de que nunca es muchas veces mejor que *ahora* mismo. Si la implementación es difícil de explicar, es una mala idea. Si la implementación es fácil de explicar, puede que sea una buena idea. Los espacios de nombres son una gran idea, ¡tengamos más de esos!"
lista_devuelta = obtener_oraciones(texto)
print(lista_devuelta)


