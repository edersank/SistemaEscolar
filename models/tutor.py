from models.usuario import Usuario
from models.mudulos import MetodosAbstractos
from models.alumno import Alumno


class Tutor(Usuario, MetodosAbstractos):
    def __init__(self, id, nombre, apellido, email, alumno: Alumno):
        super().__init__(id, nombre, apellido, email)
        self.alumno = alumno

    def imprimir_datos(self):
        print("Datos de Tutor:")
        print("--------------------------------------------------------")
        print(f"Id: {self.get_id()}")
        print(f"Nombre: {self.get_nombre()}")
        print(f"Apellido: {self.get_apellido()}")
        print(f"Correo: {self.get_email()}")
        print("--------------------------------------------------------\n")

    def mostrar_calificaciones(self):
        return self.alumno.mostrar_calificaciones()
