from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PermisoDTO(DTO):
    user_id: str = field(default_factory=str)
    rol: int = field(default_factory=int)
    permitido: bool = field(default_factory=bool)
