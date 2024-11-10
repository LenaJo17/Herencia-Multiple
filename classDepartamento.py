class Departamento:
    def __init__(self):
        self._numero_departamento = ""
        self._ubicacion = ""

    # Getters y Setters
    def get_numero_departamento(self):
        return self._numero_departamento

    def set_numero_departamento(self, numero_departamento):
        self._numero_departamento = numero_departamento

    def get_ubicacion(self):
        return self._ubicacion

    def set_ubicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def mostrar_informacion(self):
        return f"Numero_departamento: {self._numero_departamento}, Ubicacion: {self._ubicacion}"