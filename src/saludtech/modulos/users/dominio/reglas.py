"""Reglas de negocio del dominio de usuarios

En este archivo encontrará reglas de negocio del dominio de usuarios
"""

from saludtech.seedwork.dominio.reglas import ReglaNegocio
from saludtech.modulos.users.dominio.objetos_valor import NombreUsuario, Contrasena

class NombreUsuarioValido(ReglaNegocio):
    """Regla que valida que el nombre de usuario tenga un formato adecuado"""
    
    def __init__(self, username: NombreUsuario, mensaje="El nombre de usuario debe tener al menos 3 caracteres."):
        super().__init__(mensaje)
        self.username = username

    def es_valido(self) -> bool:
        return len(self.username.valor) >= 3

class ContrasenaSegura(ReglaNegocio):
    """Regla que valida que la contraseña tenga al menos 8 caracteres"""
    
    def __init__(self, password: Contrasena, mensaje="La contraseña debe tener al menos 8 caracteres."):
        super().__init__(mensaje)
        self.password = password

    def es_valido(self) -> bool:
        return len(self.password.valor) >= 8
