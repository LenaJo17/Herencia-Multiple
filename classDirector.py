from classArea import Area
from classEmpleado import Empleado

class Director(Area,Empleado):
    def __init__(self):
        super().__init__()
        self._cargo = ""
        self._unidad_responsable = ""
        self._estrategia = ""

    # Getters y Setters
    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_unidad_responsable(self):
        return self._unidad_responsable

    def set_unidad_responsable(self, unidad_responsable):
        self._unidad_responsable = unidad_responsable

    def get_estrategia(self):
        return self._estrategia

    def set_estrategia(self, estrategia):
        self._estrategia = estrategia

    def mostrar_informacion(self):
        return f"Cargo: {self._cargo}, Unidad Responsable: {self._unidad_responsable}, Estrategia: {self._estrategia}"