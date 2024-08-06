"""
1 Crear una funcion que reciba por parámetro la lista de productos y
la Recorra e Imprima cada elemento de la lista en mayusculas

2 Crear una funcion que reciba por parámetro la lista de productos y
la Recorra e Imprima cada elemento de la lista con la primer letra en
mayusculas y el resto en minusculas

3 Crear una funcion que reciba por parámetro la lista de productos y
la Recorra e Imprima cada elemento de la lista en mayusculas que este
en un indice par

4 Crear una funcion que reciba por parámetro la lista de productos y
la Recorra e Imprima cada elemento de la lista capitalizada que este
en un indice impar

5 Crear una funcion que reciba por parámetro la lista de productos,
Recorra la lista y obtenga las palabras que esten en un indice par
solamente, aplicarle mayusculas y mostrarlas todas juntas en un
nuevo string el cual separe esas palabras con un guion '-'. La cadena
resultante debe estar formateada usando el método format()
Ejemplo de salida: "MATE-HARINA-YERBA-CACAO-PATE-ARROZ-SARDINAS-CHOCLO"

6 Crear una funcion que reciba por parámetro la lista de productos,
la Recorra la lista y obtenga las palabras que esten en un indice impar
solamente y además:
A) Si tiene mas de 4 caracteres, aplicarle mayusculas.
    A.1) Si tiene mas de una letra 'A' (mayuscula o minuscula), 
        sumarla a la cantidad de a una variable contador_de_a
        que estara previamente inicializado en 0 al inicio de la funcion
B) Si tiene hasta 4 caracteres, capitalizarlas.

al resultado mostrarlas todas juntas en un nuevo string el cual 
separe esas palabras con un guion '-'. Las cadenas resultantes
deben estar formateadas con la interpolación de strings o f-strings
Ejemplo de salida: 
"Mate,HARINA,YERBA,CACAO,Pate,ARROZ,SARDINAS,CHOCLO"
"Cantidad de letras A: 6"

7 Crear una funcion que reciba por parámetro la lista de productos,
Recorra la lista, las ponga en minusculas y las concatene en un string, 
separadas por una coma ',' (Desde el primer elemento de la lista hasta 
el anteultimo inclusive). Finalmente ese string resultante deberas concatenarla al
ultimo elemento de la lista con una ' y '. Luego de eso, imprimir el 
string resultante.
Ejemplo de salida: 
"mate,cafe,harina,palmitos,yerba,mermelada,cacao,picadillo,pate,caballa,arroz,arvejas,sardinas,atún,choclo y lentejas"
"""

# Desarrollar aca las funciones:
# Ejercicio 1
def recorrer_e_imprimir_en_mayuscula(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista en mayusculas
    """
    for elemento in productos:
        print(elemento.upper(), end = " ")

# Ejercicio 2
def recorrer_e_imprimir_capitalizando(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista con la primer letra en
    mayusculas y el resto en minusculas
    """
    for elemento in productos:
        print(elemento.capitalize(), end = " ")

# Ejercicio 3
def recorrer_e_imprimir_mayusculas_indice_par(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista en mayusculas que este
    en un indice par
    """
    for elemento in range(len(productos)):
        if(elemento % 2 == 0):
            print(productos[elemento].upper(), end = " ")
        else:
            print(productos[elemento], end = " ")

# Ejercicio 4
def recorrer_e_imprimir_capitalizada_indice_impar(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos y
    la Recorra e Imprima cada elemento de la lista capitalizada que este
    en un indice impar
    """
    for elemento in range(len(productos)):
        if(elemento % 2 == 1):
            print(productos[elemento].capitalize(), end = " ")
        else:
            print(productos[elemento], end = " ")

# Ejercicio 5
def recorrer_e_imprimir_mayusculas_indice_par_formateadas(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos,
    Recorra la lista y obtenga las palabras que esten en un indice par
    solamente, aplicarle mayusculas y mostrarlas todas juntas en un
    nuevo string el cual separe esas palabras con un guion '-'. La cadena
    resultante debe estar formateada usando el método format()
    Ejemplo de salida: "MATE-HARINA-YERBA-CACAO-PATE-ARROZ-SARDINAS-CHOCLO"
    """
    palabras_mayusculas = []
    for elemento in range(len(productos)):
        if(elemento % 2 == 0):
            palabras_mayusculas.append(productos[elemento].upper())
    texto = '-'.join(palabras_mayusculas)
    resultado = "{}".format(texto)
    print(resultado)
# Ejercicio 6
def recorrer_e_imprimir_indice_impar_formateadas_y_contabilizar(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos,
    la Recorra la lista y obtenga las palabras que esten en un indice impar
    solamente y además:
    A) Si tiene mas de 4 caracteres, aplicarle mayusculas.
        A.1) Si tiene mas de una letra 'A' (mayuscula o minuscula), 
            sumarla a la cantidad de a una variable contador_de_a
            que estara previamente inicializado en 0 al inicio de la funcion
    B) Si tiene hasta 4 caracteres, capitalizarlas.

    al resultado mostrarlas todas juntas en un nuevo string el cual 
    separe esas palabras con un guion '-'. Las cadenas resultantes
    deben estar formateadas con la interpolación de strings o f-strings
    Ejemplo de salida: 
    "Mate,HARINA,YERBA,CACAO,Pate,ARROZ,SARDINAS,CHOCLO"
    "Cantidad de letras A: 6"
    """
    palabras = []
    contador_de_a = 0
    for elemento in range(len(productos)):
        if(elemento % 2 == 1):
            if(len(productos[elemento]) > 4):
                palabras.append(productos[elemento].upper())
                if('a' in productos[elemento] or 'A' in productos[elemento]):
                    contador_de_a += 1
            else:
                palabras.append(productos[elemento].capitalize())
    texto = "-".join(palabras)
    resultado = "{}".format(texto)
    print(resultado)
    print(f"Cantidad de letras: {contador_de_a}")

# Ejercicio 7
def recorrer_e_imprimir_elementos_minusculas_formateadas(productos: list[str]) -> None:
    """
    Crear una funcion que reciba por parámetro la lista de productos,
    Recorra la lista, las ponga en minusculas y las concatene en un string, 
    separadas por una coma ',' (Desde el primer elemento de la lista hasta 
    el anteultimo inclusive). Finalmente ese string resultante deberas concatenarla al
    ultimo elemento de la lista con una ' y '. Luego de eso, imprimir el 
    string resultante.
    Ejemplo de salida: 
    "mate,cafe,harina,palmitos,yerba,mermelada,cacao,picadillo,pate,caballa,arroz,arvejas,sardinas,atún,choclo y lentejas"
    """
    palabras = []
    for elemento in range(len(productos) - 1):
        palabras.append(productos[elemento].lower())
    texto_comas = ",".join(palabras)
    resultado_uno = "{}".format(texto_comas)
    resultado_dos = " y {}".format(productos[-1])
    print(f"{resultado_uno}{resultado_dos}")




if __name__ == '__main__':
    productos = [
        "mate", "caFe", "harina",
        "pAlmitos", "yerBA", "merMElada",
        "cacao", "picadillo", "pate", 
        "CABALLA", "arroz", "ArbEJaS",
        "Sardinas","atún","Choclo","lentejas"
    ]
    # Llamada de cada una de las funciones desarrolladas
    print("1. Palabras en Mayusculas:")
    recorrer_e_imprimir_en_mayuscula(productos)
    print("\n------------------------------------------------------------------------------------------------------------------")
    print("2. Palabras Capitalizadas:")
    recorrer_e_imprimir_capitalizando(productos)
    print("\n------------------------------------------------------------------------------------------------------------------")
    print("3. Palabras Pares en Mayusculas:")
    recorrer_e_imprimir_mayusculas_indice_par(productos)
    print("\n------------------------------------------------------------------------------------------------------------------")
    print("4. Palabras Impares Capitalizadas:")
    recorrer_e_imprimir_capitalizada_indice_impar(productos)
    print("\n------------------------------------------------------------------------------------------------------------------")
    print("5. Palabras Pares en un texto:")
    recorrer_e_imprimir_mayusculas_indice_par_formateadas(productos)
    print("------------------------------------------------------------------------------------------------------------------")
    print("6. Indice Impar y Contabilizar:")
    recorrer_e_imprimir_indice_impar_formateadas_y_contabilizar(productos)
    print("------------------------------------------------------------------------------------------------------------------")
    print("7. Elementos en Minusculas Formateadas:")
    recorrer_e_imprimir_elementos_minusculas_formateadas(productos)
    print("------------------------------------------------------------------------------------------------------------------")