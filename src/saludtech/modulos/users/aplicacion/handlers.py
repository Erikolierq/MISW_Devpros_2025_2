from saludtech.modulos.users.dominio.events import UsuarioCreado
from saludtech.seedwork.aplicacion.handlers import Handler
from saludtech.modulos.users.infraestructura.despachadores import Despachador

class HandlerUsuarioIntegracion(Handler):

    @staticmethod
    def handle_usuario_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-usuarios')
