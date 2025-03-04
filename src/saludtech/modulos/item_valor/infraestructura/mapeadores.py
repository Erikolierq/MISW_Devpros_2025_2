""" Mapeador para la capa de infraestructura del dominio de resultados clínicos """

from saludtech.seedwork.dominio.repositorios import Mapeador
from saludtech.modulos.item_valor.dominio.entidades import ResultadoClinico
from saludtech.modulos.item_valor.infraestructura.dto import ClinicalResult as ResultadoClinicoDTO

class MapeadorResultadoClinico(Mapeador):

    def obtener_tipo(self) -> type:
        return ResultadoClinico.__class__

    def entidad_a_dto(self, entidad: ResultadoClinico) -> ResultadoClinicoDTO:
        return ResultadoClinicoDTO(
            id=str(entidad.id),
            patient=entidad.patient,
            result=entidad.result
        )

    def dto_a_entidad(self, dto: ResultadoClinicoDTO) -> ResultadoClinico:
        return ResultadoClinico(
            id=dto.id,
            patient=dto.patient,
            result=dto.result
        )
