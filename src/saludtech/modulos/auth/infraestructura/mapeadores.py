""" Mapeador para la capa de infraestructura del dominio de autenticación """

from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.modulos.auth.dominio.entities import Autenticacion
from saludtech.modulos.auth.infraestructura.dto import AuthLog as AuthDTO

class MapeadorAuth(Mapeador):

    def obtener_tipo(self) -> type:
        return Autenticacion.__class__

    def entidad_a_dto(self, entidad: Autenticacion) -> AuthDTO:
        return AuthDTO(
            id=str(entidad.id),
            username=entidad.username,
            password=entidad.password
        )

    def dto_a_entidad(self, dto: AuthDTO) -> Autenticacion:
        return Autenticacion(
            id=dto.id,
            username=dto.username,
            password=dto.password
        )
