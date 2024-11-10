from classPersona import Persona

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self._empleado_id = ""
        self._puesto = ""
        self._salario = 0

    # Getters y Setters
    def get_empleado_id(self):
        return self._empleado_id

    def set_empleado_id(self, empleado_id):
        self._empleado_id = empleado_id

    def get_puesto(self):
        return self._puesto

    def set_puesto(self, puesto):
        self._puesto = puesto

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario

    def mostrar_informacion(self):
        persona_info = super().mostrar_informacion()
        return (f"Empleado: Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}, "
                f"Empleado_id: {self._empleado_id}, Puesto: {self._puesto}, Salario: {self._salario}")

