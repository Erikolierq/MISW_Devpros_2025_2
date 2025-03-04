from pydispatch import dispatcher

from saludtech.modulos.certificator.aplicacion.handlers import HandlerCertificatorIntegracion
from saludtech.modulos.certificator.dominio.events import PermisoValidado, PermisoDenegado

dispatcher.connect(
    HandlerCertificatorIntegracion.handle_permiso_validado, 
    signal=f'{PermisoValidado.__name__}Integracion'
)
dispatcher.connect(
    HandlerCertificatorIntegracion.handle_permiso_denegado, 
    signal=f'{PermisoDenegado.__name__}Integracion'
)
