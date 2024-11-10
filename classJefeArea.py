from classArea import Area
from classEmpleado import Empleado

class JefeArea(Area, Empleado):
    def __init__(self):
        super().__init__()
        self._proyectos_asignados = ""
        self._puesto = ""
        self._direccion = ""

    # Getters y Setters
    def get_proyectos_asignados(self):
        return self._proyectos_asignados

    def set_proyectos_asignados(self, proyectos_asignados):
        self._proyectos_asignados = proyectos_asignados

    def get_puesto(self):
        return self._puesto

    def set_puesto(self, puesto):
        self._puesto = puesto

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def mostrar_informacion(self):
        return f"Proyectos asignados: {self._proyectos_asignados}, Puesto: {self._puesto}, Direccion: {self._direccion}"
