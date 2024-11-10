from classArea import Area
from classEmpleado import Empleado

class Gerente(Area, Empleado):
    def __init__(self):
        super().__init__()
        self._codigo_gerente = ""
        self._departamentos_a_cargos = ""
        self._años_de_experiencia = 0

    # Getters y Setters
    def get_codigo_gerente(self):
        return self._codigo_gerente

    def set_codigo_gerente(self, codigo_gerente):
        self._codigo_gerente = codigo_gerente

    def get_departamentos_a_cargos(self):
        return self._departamentos_a_cargos

    def set_departamentos_a_cargos(self, departamentos_a_cargos):
        self._departamentos_a_cargos = departamentos_a_cargos

    def get_años_de_experiencia(self):
        return self._años_de_experiencia

    def set_años_de_experiencia(self, años_de_experiencia):  # También corregido en el setter
        self._años_de_experiencia = años_de_experiencia

    def mostrar_informacion(self):
        return f"Codigo gerente: {self._codigo_gerente}, Departamentos a Cargo: {self._departamentos_a_cargos}, Años de experiencia: {self._años_de_experiencia}"