# Integrantes:
# - MERO VALENTINA
# - SALINAS JOEL
# - VARGAS ANDREA
# - BENALCAZAR NATHALY

from clase_base import ServicioGym

class MembresiaVirtual(ServicioGym):
    """Membresía para entrenamiento virtual."""

    def __init__(self, nombre: str, precio_base: float, plan_videos: str, incluye_app: bool):
        super().__init__(nombre, precio_base)
        self._plan_videos = plan_videos
        self._incluye_app = incluye_app

    @property
    def plan_videos(self):
        return self._plan_videos

    @plan_videos.setter
    def plan_videos(self, valor: str):
        if not valor or not isinstance(valor, str):
            raise ValueError("El plan de videos debe ser un string válido.")
        self._plan_videos = valor

    @property
    def incluye_app(self):
        return self._incluye_app

    @incluye_app.setter
    def incluye_app(self, valor: bool):
        self._incluye_app = valor

    def calcular_costo(self):
        """Costo final con recargos por app."""
        costo = self.precio_base
        if self.incluye_app:
            costo += 10
        return costo

    def __str__(self):
        return f"{super().__str__()} - Virtual - Plan: {self.plan_videos} - App: {self.incluye_app} - Costo total: ${self.calcular_costo():.2f}"