# Integrantes:
# - MERO VALENTINA
# - SALINAS JOEL
# - VARGAS ANDREA
# - BENALCAZAR NATHALY

from abc import ABC, abstractmethod

class ServicioGym(ABC):
    """Superclase abstracta para servicios de gimnasio."""

    def __init__(self, nombre: str, precio_base: float):
        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre debe ser un string no vacío.")
        self._nombre = valor

    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor: float):
        if valor < 0:
            raise ValueError("El precio base no puede ser negativo.")
        self._precio_base = valor

    @abstractmethod
    def calcular_costo(self):
        """Calcula el costo final del servicio."""
        pass

    def __str__(self):
        return f"{self.nombre} - Precio base: ${self.precio_base:.2f}"