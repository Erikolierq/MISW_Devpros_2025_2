from saludtech.modulos.certificator.dominio.entidades import Permiso

class CertificatorAggregate:
    """
    Ejemplo de agregado para la lógica central de permisos.
    """
    def __init__(self, permission: Permiso):
        self.permission = permission

    @staticmethod
    def create(role_id: int, description: str):
        return CertificatorAggregate(Permiso(role_id, description))
