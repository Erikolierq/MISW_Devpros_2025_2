from saludtech.modulos.item_valor.dominio.events import ResultadoClinicoCreado, ResultadoConsultado
from saludtech.seedwork.aplicacion.handlers import Handler
from saludtech.modulos.item_valor.infraestructura.despachadores import Despachador

class HandlerItemValorIntegracion(Handler):

    @staticmethod
    def handle_resultado_clinico_creado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-item-valor')

    @staticmethod
    def handle_resultado_consultado(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-item-valor')
