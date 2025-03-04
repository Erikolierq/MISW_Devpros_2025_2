from saludtech.modulos.auth.dominio.events import UsuarioAutenticado, IntentoFallido
from saludtech.seedwork.aplicacion.handlers import Handler
from saludtech.modulos.auth.infraestructura.despachadores import Despachador

class HandlerAuthIntegracion(Handler):

    @staticmethod
    def handle_usuario_autenticado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-auth')

    @staticmethod
    def handle_intento_fallido(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-auth')
