from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap
from saludtech.modulos.auth.dominio.entities import Autenticacion as Sesion
from saludtech.modulos.auth.aplicacion.dto import SesionDTO

class MapeadorSesionDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> SesionDTO:
        return SesionDTO(
            user_id=externo.get('user_id'),
            token=externo.get('token'),
            expiracion=externo.get('expiracion')
        )

    def dto_a_externo(self, dto: SesionDTO) -> dict:
        return {
            "user_id": dto.user_id,
            "token": dto.token,
            "expiracion": dto.expiracion
        }

class MapeadorSesion(RepMap):
    def obtener_tipo(self) -> type:
        return Sesion.__class__

    def entidad_a_dto(self, entidad: Sesion) -> SesionDTO:
        return SesionDTO(
            user_id=str(entidad.user_id),
            token=entidad.token,
            expiracion=entidad.expiracion
        )

    def dto_a_entidad(self, dto: SesionDTO) -> Sesion:
        return Sesion(
            user_id=dto.user_id,
            token=dto.token,
            expiracion=dto.expiracion
        )
