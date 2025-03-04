from pydispatch import dispatcher

from saludtech.modulos.item_valor.aplicacion.handlers import HandlerItemValorIntegracion
from saludtech.modulos.item_valor.dominio.events import ResultadoClinicoCreado, ResultadoConsultado

dispatcher.connect(
    HandlerItemValorIntegracion.handle_resultado_clinico_creado, 
    signal=f'{ResultadoClinicoCreado.__name__}Integracion'
)
dispatcher.connect(
    HandlerItemValorIntegracion.handle_resultado_consultado, 
    signal=f'{ResultadoConsultado.__name__}Integracion'
)
