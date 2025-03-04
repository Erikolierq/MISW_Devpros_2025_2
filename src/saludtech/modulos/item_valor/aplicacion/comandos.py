from saludtech.seedwork.aplicacion.comandos import Comando
from saludtech.modulos.item_valor.aplicacion.dto import ResultadoClinicoDTO
from saludtech.modulos.item_valor.aplicacion.basecomando import CrearResultadoClinicoBaseHandler
from dataclasses import dataclass
from saludtech.seedwork.aplicacion.comandos import ejecutar_commando as comando

from saludtech.modulos.item_valor.dominio.entidades import ResultadoClinico
from saludtech.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.modulos.item_valor.aplicacion.mapeadores import MapeadorResultadoClinico
from saludtech.modulos.item_valor.infraestructura.repositorios import RepositorioResultadosClinicos

@dataclass
class CrearResultadoClinicoComando(Comando):
    patient: str
    result_text: str

class CrearResultadoClinicoHandler(CrearResultadoClinicoBaseHandler):
    
    def handle(self, comando: CrearResultadoClinicoComando):
        resultado_dto = ResultadoClinicoDTO(
            patient=comando.patient,
            result_text=comando.result_text
        )

        resultado = self.fabrica_resultados.crear_objeto(resultado_dto, MapeadorResultadoClinico())
        resultado.crear_resultado(resultado)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioResultadosClinicos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, resultado)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

@comando.register(CrearResultadoClinicoComando)
def ejecutar_comando_crear_resultado_clinico(comando: CrearResultadoClinicoComando):
    handler = CrearResultadoClinicoHandler()
    handler.handle(comando)
