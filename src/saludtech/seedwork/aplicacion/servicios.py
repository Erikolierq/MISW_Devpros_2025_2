"""
Módulo para servicios de aplicación genéricos o bases reutilizables.
"""

class ServicioAplicacionBase:
    """
    Servicio de aplicación genérico para extender en otros módulos.
    """
    def ejecutar(self, *args, **kwargs):
        raise NotImplementedError("Método ejecutar no implementado")
