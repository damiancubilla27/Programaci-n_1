''' Cubilla Damian - 1H
Escribir una función que tome un correo electrónico y elimine cualquier
carácter después del símbolo @, por ejemplo: "usuario@gmail.com" ->
"usuario".
'''
def eliminar_mail(texto:str)->str:
    indice = texto.index("@")
    retorno = texto[:indice]
    return retorno

mail_ingresado = input("Ingrese mail: ")
print(eliminar_mail(mail_ingresado))