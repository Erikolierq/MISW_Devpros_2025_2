from modulos.certificator.dominio.entidades import CertPermission
from modulos.certificator.infraestructura.dto import CertPermissionDTO

class CertificatorRepository:
    def __init__(self, session):
        self.session = session

    def get_permiso_por_rol(self, role_id: int):
        """
        Retorna una descripción de permiso para el rol, o None si no existe.
        """
        dto = self.session.query(CertPermissionDTO).get(role_id)
        if dto:
            return CertPermission(
                role_id=dto.role_id,
                description=dto.description
            )
        return None

    def add_permiso(self, permiso: CertPermission):
        dto = CertPermissionDTO(
            role_id=permiso.role_id,
            description=permiso.description
        )
        self.session.add(dto)
        self.session.commit()
        return dto
