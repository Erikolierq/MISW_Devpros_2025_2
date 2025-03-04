from saludtech.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from saludtech.seedwork.aplicacion.queries import ejecutar_query as query
from saludtech.modulos.item_valor.infraestructura.repositorios import RepositorioResultadosClinicos
from dataclasses import dataclass
from saludtech.modulos.item_valor.aplicacion.basequery import ResultadoClinicoQueryBaseHandler
from modulos.item_valor.aplicacion.mapeadores import MapeadorResultadoClinico

@dataclass
class ObtenerResultadoClinicoQuery(Query):
    id_resultado: str

class ObtenerResultadoClinicoHandler(ResultadoClinicoQueryBaseHandler):

    def handle(self, query: ObtenerResultadoClinicoQuery) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioResultadosClinicos.__class__)
        resultado = self.fabrica_resultados.crear_objeto(
            repositorio.obtener_por_id(query.id_resultado), 
            MapeadorResultadoClinico()
        )
        return QueryResultado(resultado=resultado)

@query.register(ObtenerResultadoClinicoQuery)
def ejecutar_query_obtener_resultado_clinico(query: ObtenerResultadoClinicoQuery):
    handler = ObtenerResultadoClinicoHandler()
    return handler.handle(query)
