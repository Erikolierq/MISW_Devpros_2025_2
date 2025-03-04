""" Repositorio de persistencia para autenticación """

from saludtech.config.db import db
from saludtech.modulos.auth.dominio.repositorios import RepositorioAuth
from saludtech.modulos.auth.dominio.entities import Autenticacion as Auth
from saludtech.modulos.auth.dominio.fabricas import FabricaAuth
from saludtech.modulos.auth.infraestructura.dto import AuthLog as AuthDTO
from saludtech.modulos.auth.infraestructura.mapeadores import MapeadorAuth
from uuid import UUID

class RepositorioAuthSQLite(RepositorioAuth):

    def __init__(self):
        self._fabrica_auth: FabricaAuth = FabricaAuth()

    @property
    def fabrica_auth(self):
        return self._fabrica_auth

    def obtener_por_id(self, id: UUID) -> Auth:
        auth_dto = db.session.query(AuthDTO).filter_by(id=str(id)).one_or_none()
        return self.fabrica_auth.crear_objeto(auth_dto, MapeadorAuth()) if auth_dto else None

    def obtener_por_username(self, username: str) -> Auth:
        auth_dto = db.session.query(AuthDTO).filter_by(username=username).one_or_none()
        return self.fabrica_auth.crear_objeto(auth_dto, MapeadorAuth()) if auth_dto else None

    def agregar(self, auth: Auth):
        auth_dto = self.fabrica_auth.crear_objeto(auth, MapeadorAuth())
        db.session.add(auth_dto)
        db.session.commit()
