"""Unit of Work para manejar transacciones de base de datos en los comandos CQRS."""

class UnitOfWork:
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()

    @property
    def session(self):
        return self._session

    @session.setter
    def session(self, value):
        self._session = value
