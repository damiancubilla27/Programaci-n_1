''' Cubilla Damian - 1H
Escribir una función que tome una cadena de texto y devuelva solo los
caracteres alfabéticos, eliminando cualquier número o símbolo (sólo son
válidos letras y espacios), por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”
'''
def buscar_caracteres_alfabeticos(texto:str)->str:
    texto_nuevo = []
    for elemento in texto:
        if(elemento.isalpha()):
            texto_nuevo.append(elemento)
    retorno = "".join(texto_nuevo)
    return retorno

texto_ingresado = input("Ingrese texto: ")
print(buscar_caracteres_alfabeticos(texto_ingresado))