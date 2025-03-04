from dataclasses import dataclass, field
from saludtech.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class UsuarioDTO(DTO):
    id: str = field(default_factory=str)
    username: str = field(default_factory=str)
    password: str = field(default_factory=str)
    role: int = field(default_factory=int)
