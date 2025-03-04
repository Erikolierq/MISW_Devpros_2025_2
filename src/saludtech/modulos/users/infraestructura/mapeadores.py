""" Mapeador para la capa de infraestructura del dominio de usuarios """

from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.modulos.users.dominio.entities import Usuario
from saludtech.modulos.users.infraestructura.dto import User as UsuarioDTO

class MapeadorUsuario(Mapeador):

    def obtener_tipo(self) -> type:
        return Usuario.__class__

    def entidad_a_dto(self, entidad: Usuario) -> UsuarioDTO:
        return UsuarioDTO(
            id=str(entidad.id),
            username=entidad.username,
            password=entidad.password,
            role=entidad.role
        )

    def dto_a_entidad(self, dto: UsuarioDTO) -> Usuario:
        return Usuario(
            id=dto.id,
            username=dto.username,
            password=dto.password,
            role=dto.role
        )
