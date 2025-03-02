from modulos.certificator.dominio.aggregates import CertificatorAggregate

class CertificatorFactory:
    @staticmethod
    def crear_permiso(role_id: int, description: str):
        return CertificatorAggregate.create(role_id, description)
