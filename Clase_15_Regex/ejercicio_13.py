'''Cubilla Damian
13.Crear una función que reciba un texto como parámetro y que corrija los
errores de ortografía que no cumplan con la regla ortográfica que indica que
antes de V se escribe N y que antes de B se escribe M.
Por ejemplo, si el texto es: "Mi comvicción me hace sentir que es el momento
de imvertir tiempo para finalmente enbarcar en esta nueva aventura." La
función debería devolver:
“Mi convicción me hace sentir que es el momento de invertir tiempo para
finalmente embarcar en esta nueva aventura.
'''
import re
def corregir_errores_ortograficos(texto:str)->str:
    nueva_lista = []
    lista_final = []
    lista = re.split(r" ", texto)

    for palabra in lista:
        nueva_palabra = re.sub(r"mv", "nv", palabra)
        nueva_lista.append(nueva_palabra)

    for pal in nueva_lista:
        otra_palabra = re.sub(r"nb","mb", pal)
        lista_final.append(otra_palabra)

    retorno = " ".join(lista_final)
    return retorno

texto = "Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente enbarcar en esta nueva aventura."
print(corregir_errores_ortograficos(texto))