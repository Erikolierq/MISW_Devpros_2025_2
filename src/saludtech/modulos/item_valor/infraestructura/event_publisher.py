"""Publicador de eventos usando un broker como Pulsar."""

import pulsar
from pulsar.schema import Record, String, Integer, AvroSchema

class ResultCreatedSchema(Record):
    schema_version = String(default="1.0")
    result_id = Integer()
    patient = String()
    result = String()

class EventPublisher:
    def __init__(self, pulsar_client: pulsar.Client):
        try:
            self.client = pulsar_client
            self.producer = self.client.create_producer(
                "persistent://public/default/event-topic",
                schema=AvroSchema(ResultCreatedSchema)
            )
        except Exception as e:
            print(f"Error creando el productor de eventos: {e}")
            raise

    def publish(self, event):
        # Como ejemplo, solo publicamos ResultCreatedEvent
        if event.name == "ResultCreated":
            event_data = {
                "schema_version": "1.0",
                "result_id": event.data["result_id"],
                "patient": event.data["patient"],
                "result": event.data["result"]
            }
            try:
                self.producer.send(event_data)
                print(f"Evento publicado: {event.to_json()}")
            except Exception as e:
                print(f"Error al publicar evento: {e}")
        elif event.name == "ResultQueried":
            # Podrías manejar otro tipo de evento
            pass