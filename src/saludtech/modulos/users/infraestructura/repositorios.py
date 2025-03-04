""" Repositorio de persistencia para usuarios """

from saludtech.config.db import db
from saludtech.modulos.users.dominio.repositorios import RepositorioUsuarios
from saludtech.modulos.users.dominio.entities import Usuario
from saludtech.modulos.users.dominio.fabricas import FabricaUsuarios
from saludtech.modulos.users.infraestructura.dto import User as UsuarioDTO
from saludtech.modulos.users.infraestructura.mapeadores import MapeadorUsuario
from uuid import UUID

class RepositorioUsuariosSQLite(RepositorioUsuarios):

    def __init__(self):
        self._fabrica_usuarios: FabricaUsuarios = FabricaUsuarios()

    @property
    def fabrica_usuarios(self):
        return self._fabrica_usuarios

    def obtener_por_id(self, id: UUID) -> Usuario:
        usuario_dto = db.session.query(UsuarioDTO).filter_by(id=str(id)).one_or_none()
        return self.fabrica_usuarios.crear_objeto(usuario_dto, MapeadorUsuario()) if usuario_dto else None

    def obtener_todos(self) -> list[Usuario]:
        usuarios_dto = db.session.query(UsuarioDTO).all()
        return [self.fabrica_usuarios.crear_objeto(usuario, MapeadorUsuario()) for usuario in usuarios_dto]

    def agregar(self, usuario: Usuario):
        usuario_dto = self.fabrica_usuarios.crear_objeto(usuario, MapeadorUsuario())
        db.session.add(usuario_dto)
        db.session.commit()

    def actualizar(self, usuario: Usuario):
        usuario_dto = db.session.query(UsuarioDTO).filter_by(id=str(usuario.id)).one_or_none()
        if usuario_dto:
            usuario_dto.username = usuario.username
            usuario_dto.password = usuario.password
            usuario_dto.role = usuario.role
            db.session.commit()

    def eliminar(self, usuario_id: UUID):
        db.session.query(UsuarioDTO).filter_by(id=str(usuario_id)).delete()
        db.session.commit()
