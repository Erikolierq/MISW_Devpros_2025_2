from seedwork.aplicacion.queries import QueryHandler
from saludtech.modulos.auth.infraestructura.fabricas import FabricaRepositorioAuth
from saludtech.modulos.auth.dominio.fabricas import FabricaAuth

class AuthQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorioAuth = FabricaRepositorioAuth()
        self._fabrica_auth: FabricaAuth = FabricaAuth()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_auth(self):
        return self._fabrica_auth
