from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap
from saludtech.modulos.users.dominio.entities import Usuario
from saludtech.modulos.users.aplicacion.dto import UsuarioDTO

class MapeadorUsuarioDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> UsuarioDTO:
        return UsuarioDTO(
            username=externo.get('username'),
            password=externo.get('password'),
            role=externo.get('role', 1)  
        )

    def dto_a_externo(self, dto: UsuarioDTO) -> dict:
        return {
            "username": dto.username,
            "role": dto.role
        }

class MapeadorUsuario(RepMap):
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
