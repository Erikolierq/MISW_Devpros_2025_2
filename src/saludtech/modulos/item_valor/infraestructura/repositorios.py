"""Repositorio que interactúa con la base de datos y gestiona la persistencia de los resultados clínicos."""

from modulos.item_valor.dominio.entidades import ClinicalResult
from modulos.item_valor.infraestructura.dto import ClinicalResultDTO

class ClinicalResultRepository:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, result_id: int):
        dto = self.session.query(ClinicalResultDTO).get(result_id)
        if dto:
            return ClinicalResult(
                id=dto.id,
                patient=dto.patient,
                result=dto.result
            )
        return None

    def add(self, clinical_result: ClinicalResult):
        dto = ClinicalResultDTO(
            patient=clinical_result.patient,
            result=clinical_result.result
        )
        self.session.add(dto)
        self.session.flush()  # para generar el id
        clinical_result.id = dto.id
        return dto