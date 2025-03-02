from dataclasses import dataclass

@dataclass
class ClinicalResult:
    """
    Entidad principal que representa un resultado clínico.
    """
    id: int = None
    patient: str = ""
    result: str = ""

    def to_dict(self):
        return {
            "id": self.id,
            "patient": self.patient,
            "result": self.result
        }
