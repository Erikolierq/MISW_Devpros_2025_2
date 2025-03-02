from modulos.item_valor.dominio.entidades import ClinicalResult
from modulos.item_valor.dominio.objetos_valor import PatientName, ResultText
from modulos.item_valor.dominio.events import ResultCreatedEvent


class ClinicalResultAggregate:
    """
    Ejemplo de agregado que gestiona la creación del resultado clínico y
    asegura la consistencia de sus objetos de valor.
    """
    def __init__(self, patient_vo: PatientName, result_vo: ResultText):
        self.clinical_result = ClinicalResult(
            id=None,
            patient=patient_vo.value,
            result=result_vo.value
        )

    @staticmethod
    def create(patient: str, result: str):
        patient_vo = PatientName(patient)
        result_vo = ResultText(result)
        aggregate = ClinicalResultAggregate(patient_vo, result_vo)
        return aggregate

    def to_dict(self):
        return self.clinical_result.to_dict()
