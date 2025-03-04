from saludtech.seedwork.aplicacion.queries import QueryHandler
from saludtech.modulos.users.infraestructura.fabricas import FabricaRepositorioUsuarios
from saludtech.modulos.users.dominio.fabricas import FabricaUsuarios

class UsuarioQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorioUsuarios = FabricaRepositorioUsuarios()
        self._fabrica_usuarios: FabricaUsuarios = FabricaUsuarios()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_usuarios(self):
        return self._fabrica_usuarios
