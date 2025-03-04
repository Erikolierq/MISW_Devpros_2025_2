""" Repositorio de persistencia para certificaciones """

from saludtech.config.db import db
from saludtech.modulos.certificator.dominio.repositorios import RepositorioCertificacion
from saludtech.modulos.certificator.dominio.entidades import Permiso as Certificacion
from saludtech.modulos.certificator.dominio.fabricas import FabricaCertificacion
from saludtech.modulos.certificator.infraestructura.dto import RoleValidation as CertificacionDTO
from saludtech.modulos.certificator.infraestructura.mapeadores import MapeadorCertificacion
from uuid import UUID

class RepositorioCertificacionesSQLite(RepositorioCertificacion):

    def __init__(self):
        self._fabrica_certificaciones: FabricaCertificacion = FabricaCertificacion()

    @property
    def fabrica_certificaciones(self):
        return self._fabrica_certificaciones

    def obtener_por_id(self, id: UUID) -> Certificacion:
        cert_dto = db.session.query(CertificacionDTO).filter_by(id=str(id)).one_or_none()
        return self.fabrica_certificaciones.crear_objeto(cert_dto, MapeadorCertificacion()) if cert_dto else None

    def obtener_por_usuario(self, user_id: UUID) -> Certificacion:
        cert_dto = db.session.query(CertificacionDTO).filter_by(user_id=str(user_id)).one_or_none()
        return self.fabrica_certificaciones.crear_objeto(cert_dto, MapeadorCertificacion()) if cert_dto else None
