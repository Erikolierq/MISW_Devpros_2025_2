from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ResultadoClinicoDTO(DTO):
    id: str = field(default_factory=str)
    patient: str = field(default_factory=str)
    result: str = field(default_factory=str)
