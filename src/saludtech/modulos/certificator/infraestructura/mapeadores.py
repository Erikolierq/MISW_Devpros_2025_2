""" Mapeador para la capa de infraestructura del dominio de certificación """

from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.modulos.certificator.dominio.entidades import Permiso
from saludtech.modulos.certificator.infraestructura.dto import RoleValidation as CertificacionDTO

class MapeadorCertificacion(Mapeador):

    def obtener_tipo(self) -> type:
        return Permiso.__class__

    def entidad_a_dto(self, entidad: Permiso) -> CertificacionDTO:
        return CertificacionDTO(
            id=str(entidad.id),
            role=entidad.role
        )

    def dto_a_entidad(self, dto: CertificacionDTO) -> Permiso:
        return Permiso(
            id=dto.id,
            role=dto.role
        )
