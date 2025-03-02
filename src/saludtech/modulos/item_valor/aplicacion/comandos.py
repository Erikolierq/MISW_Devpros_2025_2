from seedwork.aplicacion.comandos import ComandoBase

class CrearResultadoClinicoComando(ComandoBase):
    def __init__(self, patient, result):
        self.patient = patient
        self.result = result
