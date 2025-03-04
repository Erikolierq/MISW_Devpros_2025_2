from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class SesionDTO(DTO):
    user_id: str = field(default_factory=str)
    token: str = field(default_factory=str)
    expiracion: str = field(default_factory=str)
