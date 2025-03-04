"""Mixins del dominio de certificación

En este archivo encontrará las Mixins con capacidades 
reusables en el dominio de certificación
"""

from saludtech.modulos.certificator.dominio.entidades import Permiso

class ValidacionPermisosMixin:

    def validar_permiso_usuario(self, certificacion: Permiso, rol_requerido: int) -> bool:
        """Valida si un usuario tiene el rol necesario para una certificación."""
        return certificacion.rol >= rol_requerido
