from modulos.certificator.dominio.entidades import CertPermission

class CertificatorAggregate:
    """
    Ejemplo de agregado para la lógica central de permisos.
    """
    def __init__(self, permission: CertPermission):
        self.permission = permission

    @staticmethod
    def create(role_id: int, description: str):
        return CertificatorAggregate(CertPermission(role_id, description))
