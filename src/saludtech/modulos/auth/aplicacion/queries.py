from saludtech.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from saludtech.seedwork.aplicacion.queries import ejecutar_query as query
from saludtech.modulos.auth.infraestructura.repositorios import RepositorioAuth
from dataclasses import dataclass
from saludtech.modulos.auth.aplicacion.basequery import AuthQueryBaseHandler
from saludtech.modulos.auth.aplicacion.mapeadores import MapeadorSesion

@dataclass
class ObtenerUsuarioPorCredencialesQuery(Query):
    username: str
    password: str

class ObtenerUsuarioPorCredencialesHandler(AuthQueryBaseHandler):

    def handle(self, query: ObtenerUsuarioPorCredencialesQuery) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioAuth.__class__)
        usuario = self.fabrica_auth.crear_objeto(
            repositorio.obtener_por_credenciales(query.username, query.password), 
            MapeadorSesion()
        )
        return QueryResultado(resultado=usuario)

@query.register(ObtenerUsuarioPorCredencialesQuery)
def ejecutar_query_obtener_usuario_por_credenciales(query: ObtenerUsuarioPorCredencialesQuery):
    handler = ObtenerUsuarioPorCredencialesHandler()
    return handler.handle(query)
