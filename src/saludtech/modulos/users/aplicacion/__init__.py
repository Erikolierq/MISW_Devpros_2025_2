from pydispatch import dispatcher

from saludtech.modulos.users.aplicacion.handlers import HandlerUsuarioIntegracion
from saludtech.modulos.auth.dominio.events import UsuarioAutenticado, IntentoFallido

dispatcher.connect(
    HandlerUsuarioIntegracion.handle_usuario_creado, 
    signal=f'{UsuarioAutenticado.__name__}Integracion'
)
