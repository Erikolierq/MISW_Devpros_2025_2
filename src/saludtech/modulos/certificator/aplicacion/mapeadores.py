from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap
from saludtech.modulos.certificator.dominio.entidades import Permiso
from saludtech.modulos.certificator.aplicacion.dto import PermisoDTO

class MapeadorPermisoDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PermisoDTO:
        return PermisoDTO(
            user_id=externo.get('user_id'),
            rol=externo.get('rol'),
            permitido=externo.get('permitido')
        )

    def dto_a_externo(self, dto: PermisoDTO) -> dict:
        return {
            "user_id": dto.user_id,
            "rol": dto.rol,
            "permitido": dto.permitido
        }

class MapeadorPermiso(RepMap):
    def obtener_tipo(self) -> type:
        return Permiso.__class__

    def entidad_a_dto(self, entidad: Permiso) -> PermisoDTO:
        return PermisoDTO(
            user_id=str(entidad.user_id),
            rol=entidad.rol,
            permitido=entidad.permitido
        )

    def dto_a_entidad(self, dto: PermisoDTO) -> Permiso:
        return Permiso(
            user_id=dto.user_id,
            rol=dto.rol,
            permitido=dto.permitido
        )
