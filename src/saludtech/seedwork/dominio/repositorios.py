"""
Módulo base para repositorios (interfaces) en DDD.
"""

class RepositorioBase:
    def obtener_por_id(self, id_):
        raise NotImplementedError

    def agregar(self, entidad):
        raise NotImplementedError

    def actualizar(self, entidad):
        raise NotImplementedError

    def eliminar(self, id_):
        raise NotImplementedError
