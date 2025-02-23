from models.maestro import Maestro
from models.alumno import Alumno
from models.tutor import Tutor

# Instancias
maestro_mate = Maestro(1122, "Alejandro", "Ponce", "eponce@edu.correo.com")
alumno_mateo = Alumno("8877", "Mateo", "Morales", "pelonmateo@correo.com")
tutora_ale = Tutor(2312, "Alejandra", "Rivera",
                   "alriver@edu.correo.com", alumno_mateo)

# Test Maestro
maestro_mate.imprimir_datos()

# Test Alumno
alumno_mateo.imprimir_datos()
alumno_mateo.mostrar_calificaciones()
# alumno_mateo.guardar_calificacion(8.7)
# alumno_mateo.guardar_calificacion(9.5)
# alumno_mateo.mostrar_calificaciones()

# Test tutor
tutora_ale.imprimir_datos()
tutora_ale.mostrar_calificaciones()
