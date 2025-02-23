from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, id, nombre, apellido, email):
        self.__id = id
        self.nombre = nombre
        self.apellido = apellido
        self.__email = email

    # Metodo de static
    @abstractmethod
    def imprimir_datos(self):
        pass

    # Metodos getter y setter id
    def get_id(self):
        return self.__id

    # Metodos getter y setter nombre
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    # Metodos getter y setter apellido
    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    # Metodos getter y setter email
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email
