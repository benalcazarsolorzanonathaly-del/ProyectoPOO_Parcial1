# Integrantes:
# - MERO VALENTINA
# - SALINAS JOEL
# - VARGAS ANDREA
# - BENALCAZAR NATHALY

from clase_base import ServicioGym

class MembresiaPresencial(ServicioGym):
    """Membresía para uso presencial en el gimnasio."""

    def __init__(self, nombre: str, precio_base: float, acceso_sala: bool, acceso_clases: bool):
        super().__init__(nombre, precio_base)
        self._acceso_sala = acceso_sala
        self._acceso_clases = acceso_clases

    @property
    def acceso_sala(self):
        return self._acceso_sala

    @acceso_sala.setter
    def acceso_sala(self, valor: bool):
        self._acceso_sala = valor

    @property
    def acceso_clases(self):
        return self._acceso_clases

    @acceso_clases.setter
    def acceso_clases(self, valor: bool):
        self._acceso_clases = valor

    def calcular_costo(self):
        """Costo final con recargos por servicios adicionales."""
        costo = self.precio_base
        if self.acceso_sala:
            costo += 20
        if self.acceso_clases:
            costo += 15
        return costo

    def __str__(self):
        return f"{super().__str__()} - Presencial - Sala: {self.acceso_sala} - Clases: {self.acceso_clases} - Costo total: ${self.calcular_costo():.2f}"