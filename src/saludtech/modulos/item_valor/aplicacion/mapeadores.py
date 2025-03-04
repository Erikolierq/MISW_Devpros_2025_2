from saludtech.seedwork.aplicacion.dto import Mapeador as AppMap
from saludtech.seedwork.dominio.repositorios import Mapeador as RepMap
from saludtech.modulos.item_valor.dominio.entidades import ResultadoClinico
from saludtech.modulos.item_valor.aplicacion.dto import ResultadoClinicoDTO

class MapeadorResultadoClinicoDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> ResultadoClinicoDTO:
        return ResultadoClinicoDTO(
            id=externo.get('id'),
            patient=externo.get('patient'),
            result=externo.get('result')
        )

    def dto_a_externo(self, dto: ResultadoClinicoDTO) -> dict:
        return {
            "id": dto.id,
            "patient": dto.patient,
            "result": dto.result
        }

class MapeadorResultadoClinico(RepMap):
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
