"""Mixins del dominio de autenticación

En este archivo encontrará las Mixins con capacidades 
reusables en el dominio de autenticación
"""

from saludtech.modulos.auth.dominio.entities import Autenticacion

class ManejoSesionMixin:

    def cerrar_sesion(self, sesion: Autenticacion) -> bool:
        """Cierra una sesión, invalidando su estado."""
        sesion.activa = False
        return True

    def validar_sesion_activa(self, sesion: Autenticacion) -> bool:
        """Verifica si la sesión está activa."""
        return sesion.activa
