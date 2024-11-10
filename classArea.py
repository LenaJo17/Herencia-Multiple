from classDepartamento import Departamento

class Area(Departamento):
    def __init__(self):
        super().__init__()
        self._objetivo_area =  ""
        self._lider_area = ""
        self._numero_empleados_area = ""

        # Getters y Setters

    def get_objetivo_area(self):
        return self._objetivo_area

    def set_objetivo_area(self, objetivo_area):
        self._objetivo_area = objetivo_area

    def get_lider_area(self):
        return self._lider_area

    def set_lider_area(self, lider_area):
        self._lider_area = lider_area

    def get_numero_empleados_area(self):
        return self._numero_empleados_area

    def set_numero_empleados_area(self, numeros_empleados_area):
        self._numero_empleados_area = numeros_empleados_area

    def mostrar_informacion(self):
        return f"Objetivo area: {self._objetivo_area}, Lider area: {self._objetivo_area}, Numero empleados area: {self._numero_empleados_area}"




