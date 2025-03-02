from seedwork.aplicacion.queries import QueryBase

class ObtenerResultadoClinicoQuery(QueryBase):
    def __init__(self, result_id):
        self.result_id = result_id
