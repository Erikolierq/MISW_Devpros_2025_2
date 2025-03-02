import json
import datetime

class DomainEvent:
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

class UserLoggedInEvent(DomainEvent):
    def __init__(self, user_id, username, version=1):
        super().__init__(
            "UserLoggedIn",
            {
                "user_id": user_id,
                "username": username
            },
            version
        )

class UserLoggedOutEvent(DomainEvent):
    def __init__(self, user_id, version=1):
        super().__init__(
            "UserLoggedOut",
            {
                "user_id": user_id
            },
            version
        )
