"""Reglas de negocio del dominio de certificación

En este archivo encontrará reglas de negocio del dominio de certificación
"""

from saludtech.seedwork.dominio.reglas import ReglaNegocio
from saludtech.modulos.certificator.dominio.objetos_valor import Certificado, TipoPermiso

class PermisoValido(ReglaNegocio):
    """Regla que valida que un usuario tenga permiso para realizar una acción"""

    def __init__(self, certificado: Certificado, mensaje="El usuario no tiene permisos suficientes."):
        super().__init__(mensaje)
        self.certificado = certificado

    def es_valido(self) -> bool:
        return self.certificado.rol == 2  # Solo el rol 2 tiene permisos
