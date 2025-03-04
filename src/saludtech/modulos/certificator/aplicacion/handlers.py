from saludtech.modulos.certificator.dominio.events import PermisoValidado, PermisoDenegado
from saludtech.seedwork.aplicacion.handlers import Handler
from saludtech.modulos.certificator.infraestructura.despachadores import Despachador

class HandlerCertificatorIntegracion(Handler):

    @staticmethod
    def handle_permiso_validado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-certificator')

    @staticmethod
    def handle_permiso_denegado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-certificator')
