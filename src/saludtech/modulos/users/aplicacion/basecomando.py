from saludtech.seedwork.aplicacion.comandos import ComandoHandler
from saludtech.modulos.users.infraestructura.fabricas import FabricaRepositorioUsuarios
from saludtech.modulos.users.dominio.fabricas import FabricaUsuarios

class CrearUsuarioBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorioUsuarios = FabricaRepositorioUsuarios()
        self._fabrica_usuarios: FabricaUsuarios = FabricaUsuarios()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio

    @property
    def fabrica_usuarios(self):
        return self._fabrica_usuarios
