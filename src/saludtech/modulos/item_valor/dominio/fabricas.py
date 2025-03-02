from modulos.item_valor.dominio.aggregates import ClinicalResultAggregate

class ClinicalResultFactory:
    """
    Fábrica para crear el agregado de resultados clínicos.
    """
    @staticmethod
    def crear_resultado_clinico(patient: str, result: str):
        return ClinicalResultAggregate.create(patient, result)
