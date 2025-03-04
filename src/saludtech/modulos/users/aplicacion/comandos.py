from saludtech.seedwork.aplicacion.comandos import Comando
from saludtech.modulos.users.aplicacion.dto import UsuarioDTO
from saludtech.modulos.users.aplicacion.basecomando import CrearUsuarioBaseHandler
from dataclasses import dataclass
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludtech.modulos.users.dominio.entities import Usuario
from saludtech.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.modulos.users.aplicacion.mapeadores import MapeadorUsuario
from saludtech.modulos.users.infraestructura.repositorios import RepositorioUsuarios

@dataclass
class CrearUsuarioComando(Comando):
    username: str
    password: str
    role: int

class CrearUsuarioHandler(CrearUsuarioBaseHandler):
    
    def handle(self, comando: CrearUsuarioComando):
        usuario_dto = UsuarioDTO(
            username=comando.username,
            password=comando.password,
            role=comando.role
        )

        usuario = self.fabrica_usuarios.crear_objeto(usuario_dto, MapeadorUsuario())
        Usuario.crear_usuario(usuario)
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioUsuarios.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, usuario)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(CrearUsuarioComando)
def ejecutar_comando_crear_usuario(comando: CrearUsuarioComando):
    handler = CrearUsuarioHandler()
    handler.handle(comando)
