from saludtech.seedwork.aplicacion.queries import QueryHandler
from saludtech.modulos.item_valor.infraestructura.fabricas import FabricaRepositorioResultadosClinicos
from saludtech.modulos.item_valor.dominio.fabricas import FabricaResultadosClinicos

class ResultadoClinicoQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorioResultadosClinicos = FabricaRepositorioResultadosClinicos()
        self._fabrica_resultados: FabricaResultadosClinicos = FabricaResultadosClinicos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_resultados(self):
        return self._fabrica_resultados
