# Integrantes:
# - MERO VALENTINA
# - SALINAS JOEL
# - VARGAS ANDREA
# - BENALCAZAR NATHALY

from clase_base import ServicioGym

class GestorGym:
    """Clase para gestionar servicios del gimnasio."""

    def __init__(self):
        self._servicios = []

    def agregar_servicio(self, servicio: ServicioGym):
        """Agrega un servicio a la lista."""
        self._servicios.append(servicio)

    def calcular_total_ingresos(self, servicios: list[ServicioGym]):
        """Método polimórfico 1: Suma los costos de todos los servicios."""
        total = 0
        for s in servicios:
            total += s.calcular_costo()
        return total

    def generar_reporte(self, servicios: list[ServicioGym]):
        """Método polimórfico 2: Genera un reporte de servicios."""
        reporte = []
        for s in servicios:
            reporte.append(str(s))
        return "\n".join(reporte)

    def __str__(self):
        return f"Gestor con {len(self._servicios)} servicios registrados."