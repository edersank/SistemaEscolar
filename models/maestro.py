from models.usuario import Usuario


class Maestro(Usuario):
    def __init__(self, id, nombre, apellido, email):
        super().__init__(id, nombre, apellido, email)

    def imprimir_datos(self):
        print("Datos de maestro:")
        print("--------------------------------------------------------")
        print(f"Id: {self.get_id()}")
        print(f"Nombre: {self.get_nombre()}")
        print(f"Apellido: {self.get_apellido()}")
        print(f"Correo: {self.get_email()}")
        print("--------------------------------------------------------\n")
