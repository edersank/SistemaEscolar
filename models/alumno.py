from models.usuario import Usuario


class Alumno(Usuario):
    def __init__(self, id, nombre, apellido, email):
        super().__init__(id, nombre, apellido, email)
        self.calificacion = []

    def imprimir_datos(self):
        print("Datos de alumno:")
        print("--------------------------------------------------------")
        print(f"Id: {self.get_id()}")
        print(f"Nombre: {self.get_nombre()}")
        print(f"Apellido: {self.get_apellido()}")
        print(f"Correo: {self.get_email()}")
        print("--------------------------------------------------------\n")

    def guardar_calificacion(self, calificacion):
        self.calificacion.append(calificacion)

    def mostrar_calificaciones(self):
        calificaiones = self.calificacion

        print(
            f"Calificaciones de alumno: {self.get_nombre()} \t Id:{self.get_id()} ")
        print("--------------------------------------------------------")

        if len(calificaiones) is not 0:
            for nota in calificaiones:
                print(nota)

        else:
            print("Lo sentimos, aún no hay calificiaciones registradas")

        print("--------------------------------------------------------\n")
