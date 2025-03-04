from saludtech.seedwork.aplicacion.queries import QueryHandler
from saludtech.modulos.certificator.infraestructura.fabricas import FabricaRepositorioCertificacion
from saludtech.modulos.certificator.dominio.fabricas import FabricaCertificacion

class PermisosQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorioCertificacion = FabricaRepositorioCertificacion()
        self._fabrica_permisos: FabricaCertificacion = FabricaCertificacion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_permisos(self):
        return self._fabrica_permisos
