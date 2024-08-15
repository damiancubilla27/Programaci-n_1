class Personaje:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_final, presupuesto, estado) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio
        self.__fecha_final = fecha_final
        self.__presupuesto = presupuesto
        self.__estado = estado

    def saludar(self)->None:
        print(f"Hola, me llamo: {self.__nombre}")