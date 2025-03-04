from pydispatch import dispatcher

from .handlers import HandlerAuthIntegracion
from saludtech.modulos.auth.dominio.events import UsuarioAutenticado, IntentoFallido

dispatcher.connect(
    HandlerAuthIntegracion.handle_usuario_autenticado, 
    signal=f'{UsuarioAutenticado.__name__}Integracion'
)
dispatcher.connect(
    HandlerAuthIntegracion.handle_intento_fallido, 
    signal=f'{IntentoFallido.__name__}Integracion'
)
