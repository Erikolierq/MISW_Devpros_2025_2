import pulsar
from pulsar.schema import Record, String, Integer, AvroSchema

class UserLoggedInSchema(Record):
    schema_version = String(default="1.0")
    user_id = Integer()
    username = String()

class UserLoggedOutSchema(Record):
    schema_version = String(default="1.0")
    user_id = Integer()

class EventPublisher:
    def __init__(self, pulsar_client: pulsar.Client):
        try:
            self.client = pulsar_client
            self.producer_login = self.client.create_producer(
                "persistent://public/default/auth-loggedin-topic",
                schema=AvroSchema(UserLoggedInSchema)
            )
            self.producer_logout = self.client.create_producer(
                "persistent://public/default/auth-loggedout-topic",
                schema=AvroSchema(UserLoggedOutSchema)
            )
        except Exception as e:
            print(f"Error creando el productor de eventos: {e}")
            raise

    def publish(self, event):
        if event.name == "UserLoggedIn":
            data = {
                "schema_version": "1.0",
                "user_id": event.data["user_id"],
                "username": event.data["username"]
            }
            try:
                self.producer_login.send(data)
                print(f"Evento publicado: {event.to_json()}")
            except Exception as e:
                print(f"Error al publicar evento: {e}")
        elif event.name == "UserLoggedOut":
            data = {
                "schema_version": "1.0",
                "user_id": event.data["user_id"]
            }
            try:
                self.producer_logout.send(data)
                print(f"Evento publicado: {event.to_json()}")
            except Exception as e:
                print(f"Error al publicar evento: {e}")
