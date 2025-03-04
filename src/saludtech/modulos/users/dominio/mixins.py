"""Mixins del dominio de usuarios

En este archivo encontrará las Mixins con capacidades 
reusables en el dominio de usuarios
"""

from saludtech.modulos.users.dominio.entities import Usuario

class FiltradoUsuariosMixin:

    def filtrar_por_rol(self, usuarios: list[Usuario], rol: int) -> list[Usuario]:
        """Filtra los usuarios según su rol."""
        return [usuario for usuario in usuarios if usuario.rol == rol]

    def obtener_usuario_por_nombre(self, usuarios: list[Usuario], username: str) -> Usuario | None:
        """Obtiene un usuario por su nombre de usuario."""
        return next((usuario for usuario in usuarios if usuario.username == username), None)
