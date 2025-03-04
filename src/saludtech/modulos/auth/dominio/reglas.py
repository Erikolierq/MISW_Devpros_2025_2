"""Reglas de negocio del dominio de autenticación

En este archivo encontrará reglas de negocio del dominio de autenticación
"""

from saludtech.seedwork.dominio.reglas import ReglaNegocio
from saludtech.modulos.auth.dominio.objetos_valor import Credenciales

class CredencialesValidas(ReglaNegocio):
    """Regla que valida que las credenciales contengan un username y password no vacíos"""

    def __init__(self, credenciales: Credenciales, mensaje="Las credenciales no pueden estar vacías."):
        super().__init__(mensaje)
        self.credenciales = credenciales

    def es_valido(self) -> bool:
        return bool(self.credenciales.username and self.credenciales.password)
