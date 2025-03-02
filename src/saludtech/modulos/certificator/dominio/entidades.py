from dataclasses import dataclass

@dataclass
class CertPermission:
    """
    Entidad que representa un permiso para un rol específico.
    """
    role_id: int
    description: str
