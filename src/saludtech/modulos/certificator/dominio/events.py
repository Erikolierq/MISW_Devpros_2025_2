import json
import datetime

class DomainEvent:
    """
    Clase base para los eventos de dominio.
    """
    def __init__(self, name, data, version=1):
        self.name = name
        self.data = data
        self.version = version
        self.timestamp = datetime.datetime.utcnow().isoformat()

    def to_json(self):
        return json.dumps({
            "name": self.name,
            "data": self.data,
            "version": self.version,
            "timestamp": self.timestamp
        })

class PermissionValidatedEvent(DomainEvent):
    def __init__(self, user_role, allowed, version=1):
        super().__init__(
            "PermissionValidated",
            {
                "user_role": user_role,
                "allowed": allowed
            },
            version
        )
