class Clinica:
    def __init__(self, razon_social):
        self.__razon_social = razon_social
        self.__lista_pacientes = []
        self.__lista_turnos = []
        self.__especialidades = {}
        self.__obras_sociales_validas = {}
        self.__recaudacion = 0.0
        self.__hay_pacientes_sin_atencion = False

    @property
    def get_razon_social(self):
        return self.__razon_social
    
    @property
    def get_lista_pacientes(self):
        return self.__lista_pacientes
    
    @property
    def get_lista_turnos(self):
        return self.__lista_turnos
    
    @property
    def get_especialidades(self):
        return self.__especialidades
    
    @property
    def get_obras_sociales(self):
        return self.__obras_sociales_validas
    
    @property
    def get_recaudacion(self):
        return self.__recaudacion
    
    @property
    def get_pacientes_sin_atencion(self):
        return self.__hay_pacientes_sin_atencion

    @get_razon_social.setter
    def set_razon_social(self, nueva_razon_social):
        self.__razon_social = nueva_razon_social

    @get_lista_pacientes.setter
    def set_lista_pacientes(self, nueva_lista_pacientes):
        self.__lista_pacientes = nueva_lista_pacientes
    
    @get_lista_turnos.setter
    def set_lista_turnos(self, nueva_lista_pacientes):
        self.__lista_turnos = nueva_lista_pacientes

    @get_lista_turnos.setter
    def set_lista_turnos(self, nueva_lista_turnos):
        self.__lista_turnos = nueva_lista_turnos

    @get_especialidades.setter
    def set_especialidades(self, nuevas_especialidades):
        self.__especialidades = nuevas_especialidades

    @get_obras_sociales.setter
    def set_obras_sociales(self, nueva_obras_sociales):
        self.__obras_sociales_validas = nueva_obras_sociales

    @get_recaudacion.setter
    def set_recaudacion(self, nueva_recaudacion):
        self.__recaudacion = nueva_recaudacion

    @get_pacientes_sin_atencion.setter
    def set_pacientes_sin_atencion(self, nuevos_pacientes):
        self.__hay_pacientes_sin_atencion = nuevos_pacientes