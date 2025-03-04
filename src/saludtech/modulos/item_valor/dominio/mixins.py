"""Mixins del dominio de resultados clínicos

En este archivo encontrará las Mixins con capacidades 
reusables en el dominio de resultados clínicos
"""

from saludtech.modulos.item_valor.dominio.entidades import ResultadoClinico

class FiltradoResultadosMixin:

    def filtrar_resultados_por_paciente(self, resultados: list[ResultadoClinico], paciente_id: str) -> list[ResultadoClinico]:
        """Filtra los resultados clínicos por paciente."""
        return [resultado for resultado in resultados if resultado.paciente_id == paciente_id]

    def obtener_ultimo_resultado(self, resultados: list[ResultadoClinico]) -> ResultadoClinico | None:
        """Obtiene el último resultado clínico registrado."""
        return max(resultados, key=lambda r: r.fecha, default=None)
