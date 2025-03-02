import pulsar
from pulsar.schema import Record, String, Boolean, Integer, AvroSchema

class PermissionValidatedSchema(Record):
    schema_version = String(default="1.0")
    user_role = Integer()
    allowed = Boolean()

class EventPublisher:
    def __init__(self, pulsar_client: pulsar.Client):
        try:
            self.client = pulsar_client
            self.producer = self.client.create_producer(
                "persistent://public/default/certificator-topic",
                schema=AvroSchema(PermissionValidatedSchema)
            )
        except Exception as e:
            print(f"Error creando el productor de eventos: {e}")
            raise

    def publish(self, event):
        if event.name == "PermissionValidated":
            event_data = {
                "schema_version": "1.0",
                "user_role": event.data["user_role"],
                "allowed": event.data["allowed"]
            }
            try:
                self.producer.send(event_data)
                print(f"Evento publicado: {event.to_json()}")
            except Exception as e:
                print(f"Error al publicar evento: {e}")

        # Si tuvieras más tipos de eventos, podrías manejarlo con if/elif/else
