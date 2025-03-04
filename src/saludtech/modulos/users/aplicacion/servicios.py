from saludtech.seedwork.aplicacion.servicios import Servicio
from saludtech.modulos.users.dominio.entities import Usuario
from saludtech.modulos.users.dominio.fabricas import FabricaUsuarios
from saludtech.modulos.users.infraestructura.fabricas import FabricaRepositorioUsuarios
from saludtech.modulos.users.infraestructura.repositorios import RepositorioUsuarios
from saludtech.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.modulos.users.aplicacion.mapeadores import MapeadorUsuario
from saludtech.modulos.users.aplicacion.dto import UsuarioDTO

class ServicioUsuario(Servicio):

    def __init__(self):
        self._fabrica_repositorio = FabricaRepositorioUsuarios()
        self._fabrica_usuarios = FabricaUsuarios()

    def crear_usuario(self, usuario_dto: UsuarioDTO) -> UsuarioDTO:
        usuario = self._fabrica_usuarios.crear_objeto(usuario_dto, MapeadorUsuario())
        usuario.crear_usuario(usuario)

        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioUsuarios.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, usuario)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self._fabrica_usuarios.crear_objeto(usuario, MapeadorUsuario())

    def obtener_usuario_por_id(self, id) -> UsuarioDTO:
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioUsuarios.__class__)
        return self._fabrica_usuarios.crear_objeto(repositorio.obtener_por_id(id), MapeadorUsuario())
