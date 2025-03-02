"""
Módulo base para Unit of Work.
"""

class UnitOfWorkBase:
    """
    Clase base para la implementación de un Unit of Work.
    """
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()

    def commit(self):
        raise NotImplementedError

    def rollback(self):
        raise NotImplementedError
