"""Permite almacenar los eventos en la base de datos y/o publicarlos en un broker."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, JSON, DateTime, Boolean
from saludtech.config.db import db
import json

class EventStore(db.Model):
    __tablename__ = 'event_store'

    id = Column(Integer, primary_key=True)
    event_name = Column(String(100), nullable=False)
    event_data = Column(JSON, nullable=False)
    event_version = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    processed = Column(Boolean, default=False)

class EventStoreRepository:
    def __init__(self, session):
        self.session = session

    def save_event(self, event):
        new_event = EventStore(
            event_name=event.name,
            event_data=event.data,
            event_version=event.version,
            processed=False
        )
        self.session.add(new_event)
        self.session.commit()

    def mark_event_processed(self, event_id: int):
        ev = self.session.query(EventStore).get(event_id)
        if ev:
            ev.processed = True
            self.session.commit()

    def is_event_processed(self, event):
        # Ejemplo sencillo, buscar por event_name y data
        result = self.session.query(EventStore).filter_by(
            event_name=event.name,
            event_data=event.data
        ).first()
        return bool(result and result.processed)