import pulsar
from pulsar.schema import Record, String, Integer, AvroSchema

class UserCreatedSchema(Record):
    schema_version = String(default="1.0")
    user_id = Integer()
    username = String()
    role = Integer()

class UserUpdatedSchema(Record):
    schema_version = String(default="1.0")
    user_id = Integer()
    username = String()
    role = Integer()

class EventPublisher:
    def __init__(self, pulsar_client: pulsar.Client):
        try:
            self.client = pulsar_client
            # Podrías tener 2 productores, uno para each event, o uno genérico:
            self.producer_created = self.client.create_producer(
                "persistent://public/default/users-created-topic",
                schema=AvroSchema(UserCreatedSchema)
            )
            self.producer_updated = self.client.create_producer(
                "persistent://public/default/users-updated-topic",
                schema=AvroSchema(UserUpdatedSchema)
            )
        except Exception as e:
            print(f"Error creando el productor de eventos: {e}")
            raise

    def publish(self, event):
        # Ejemplo: manejar UserCreated y UserUpdated
        if event.name == "UserCreated":
            event_data = {
                "schema_version": "1.0",
                "user_id": event.data["user_id"],
                "username": event.data["username"],
                "role": event.data["role"]
            }
            try:
                self.producer_created.send(event_data)
                print(f"Evento publicado: {event.to_json()}")
            except Exception as e:
                print(f"Error al publicar evento: {e}")

        elif event.name == "UserUpdated":
            event_data = {
                "schema_version": "1.0",
                "user_id": event.data["user_id"],
                "username": event.data["username"],
                "role": event.data["role"]
            }
            try:
                self.producer_updated.send(event_data)
                print(f"Evento publicado: {event.to_json()}")
            except Exception as e:
                print(f"Error al publicar evento: {e}")
