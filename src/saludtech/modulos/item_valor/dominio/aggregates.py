from saludtech.modulos.item_valor.dominio.entidades import ResultadoClinico
from saludtech.modulos.item_valor.dominio.objetos_valor import Paciente, ResultadoClinico
from saludtech.modulos.item_valor.dominio.events import ResultadoClinicoCreado


class ClinicalResultAggregate:
    """
    Ejemplo de agregado que gestiona la creación del resultado clínico y
    asegura la consistencia de sus objetos de valor.
    """
    def __init__(self, patient_vo: Paciente, result_vo: ResultadoClinico):
        self.clinical_result = ResultadoClinico(
            id=None,
            patient=patient_vo.value,
            result=result_vo.value
        )

    @staticmethod
    def create(patient: str, result: str):
        patient_vo = Paciente(patient)
        result_vo = ResultadoClinico(result)
        aggregate = ClinicalResultAggregate(patient_vo, result_vo)
        return aggregate

    def to_dict(self):
        return self.clinical_result.to_dict()
