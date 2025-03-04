from saludtech.seedwork.aplicacion.servicios import Servicio
from saludtech.modulos.item_valor.dominio.entidades import ResultadoClinico
from saludtech.modulos.item_valor.dominio.fabricas import FabricaResultadosClinicos
from saludtech.modulos.item_valor.infraestructura.fabricas import FabricaRepositorioResultadosClinicos
from saludtech.modulos.item_valor.infraestructura.repositorios import RepositorioResultadosClinicos
from saludtech.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from saludtech.modulos.item_valor.aplicacion.mapeadores import MapeadorResultadoClinico
from saludtech.modulos.item_valor.aplicacion.dto import ResultadoClinicoDTO

class ServicioResultadoClinico(Servicio):

    def __init__(self):
        self._fabrica_repositorio = FabricaRepositorioResultadosClinicos()
        self._fabrica_resultados = FabricaResultadosClinicos()

    def crear_resultado(self, resultado_dto: ResultadoClinicoDTO) -> ResultadoClinicoDTO:
        resultado = self._fabrica_resultados.crear_objeto(resultado_dto, MapeadorResultadoClinico())

        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioResultadosClinicos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, resultado)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()

        return self._fabrica_resultados.crear_objeto(resultado, MapeadorResultadoClinico())

    def obtener_resultado_por_id(self, id) -> ResultadoClinicoDTO:
        repositorio = self._fabrica_repositorio.crear_objeto(RepositorioResultadosClinicos.__class__)
        return self._fabrica_resultados.crear_objeto(repositorio.obtener_por_id(id), MapeadorResultadoClinico())
