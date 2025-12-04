# Integrantes:
# - MERO VALENTINA
# - SALINAS JOEL
# - VARGAS ANDREA
# - BENALCAZAR NATHALY

class Cliente:
    """Clase para representar un cliente del gimnasio."""

    def __init__(self, id_cliente: int, nombre: str, telefono: str):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._telefono = telefono

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, valor: int):
        if valor < 0:
            raise ValueError("ID no puede ser negativo.")
        self._id_cliente = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValueError("Nombre debe ser string no vacío.")
        self._nombre = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValueError("Teléfono debe ser string no vacío.")
        self._telefono = valor

    def __str__(self):
        return f"Cliente {self.id_cliente}: {self.nombre} - Tel: {self.telefono}"